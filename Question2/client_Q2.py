import socket
import sys

HOST = '127.0.0.1'  # Update this if running on localhost or another machine
PORT = 12345

def run_client(stringg):
    """Connects to the server, sends a request, and prints the response."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((HOST, PORT))
            client_socket.sendall(stringg.encode())
            response = client_socket.recv(1024).decode()
            print(f"Server response: {response}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python/python3 client.py <message>")
        sys.exit(1)
    run_client(sys.argv[1])
