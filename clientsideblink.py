import cv2
import socket
import time

# Function to simulate blink detection (replace with actual detection logic)
def detect_blinks():
    # Simulate a random blink count (use actual blink detection here)
    import random
    return random.randint(5, 20)

# Socket client to send blink data
def send_blink_data(host, port):
    while True:
        try:
            blinks = detect_blinks()
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((host, port))
                message = f"Blinks: {blinks}"
                s.sendall(message.encode('utf-8'))
            time.sleep(120)  # Send data every 2 minutes
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    HOST = "127.0.0.1"  # Replace with server IP
    PORT = 5000
    send_blink_data(HOST, PORT)
