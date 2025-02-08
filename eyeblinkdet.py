import cv2
import socket
import time
import threading
import streamlit as st
from collections import defaultdict
import json

# Global variables
blink_data = defaultdict(list)  # Store blink data per client
health_alerts = {}

# Streamlit UI setup
def display_ui():
    st.title("Blink Monitor Dashboard")

    # Real-time blinking trends
    st.subheader("Blinking Trends")
    if blink_data:
        for client, blinks in blink_data.items():
            st.line_chart({client: blinks})
    else:
        st.write("No data available yet.")

    # Health alerts
    st.subheader("Health Alerts")
    if health_alerts:
        for client, alert in health_alerts.items():
            st.error(f"{client}: {alert}")
    else:
        st.write("No health alerts.")

# Socket listener for blink data
def socket_listener(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"Server running on {host}:{port}")

        while True:
            client_socket, addr = server_socket.accept()
            with client_socket:
                data = client_socket.recv(1024).decode('utf-8')
                if data:
                    client_id = f"Client {addr[0]}:{addr[1]}"
                    blinks = int(data.split(': ')[1])
                    blink_data[client_id].append(blinks)

                    # Health alert if blinks < 10 in 2 minutes
                    if blinks < 10:
                        health_alerts[client_id] = f"Low blinking detected ({blinks} blinks in 2 minutes). Stay hydrated and take breaks!"
                    else:
                        health_alerts.pop(client_id, None)

# Main function
def main():
    HOST = '0.0.0.0'
    PORT = 5000

    # Start socket listener in a separate thread
    threading.Thread(target=socket_listener, args=(HOST, PORT), daemon=True).start()

    # Display Streamlit UI
    display_ui()

if __name__ == "__main__":
    main()
