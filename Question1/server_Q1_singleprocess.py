import socket
HOST = '127.0.0.1'
PORT = 12345

def handle_request(request):
    try:
        choice, data = request.split(",", 1)
        if choice == '1':
            return data.swapcase()
        elif choice == '2':
            return str(eval(data))
        elif choice == '3':
            return data[::-1]
        else:
            return "Invalid Choice"
    except Exception as e:
        return str(e)

def process_client(conn, addr):
    print(f"Connected by {addr}")
    request = conn.recv(1024).decode()
    response = handle_request(request)
    # time.sleep(3)
    conn.sendall(response.encode())
    conn.close()
    print(f"Connection closed {addr}")

def single_process_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(100)
        print("Running Single-Process Server...")

        while True:
            conn, addr = server_socket.accept()
            process_client(conn, addr)


if __name__ == "__main__":
    single_process_server()