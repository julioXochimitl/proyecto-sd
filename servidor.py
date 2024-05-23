import socket
import threading

def send_audio(client_socket):
    with open('test.wav', 'rb') as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            try:
                client_socket.send(data)
            except Exception as e:
                print("Error al enviar audio:", e)
                break
    client_socket.close()

def handle_client(client_socket, address):
    print(f"Conexión establecida desde {address}")
    send_audio(client_socket)
    print(f"Conexión cerrada desde {address}")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 9999))
    server_socket.listen(5)

    print("Servidor escuchando en el puerto 9999...")

    while True:
        client_socket, address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()

if __name__ == "__main__":
    main()
