import socket

def client():
    host = '127.0.0.1'
    port = 12345

    while True:
        print("\nMenu:")
        print("1. Change case of string")
        print("2. Evaluate mathematical expression")
        print("3. Reverse string")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '4':
            print("Exiting client.")
            break

        data = input("Enter input data: ")

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))

            client_socket.sendall(f"{choice},{data}".encode())

            response = client_socket.recv(1024).decode()
            print(f"Server Response: {response}")
            print('Connection to Server Closed')

if __name__ == "__main__":
    client()