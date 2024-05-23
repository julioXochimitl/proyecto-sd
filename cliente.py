import socket
import pyaudio

def play_audio(client_socket):
    print("Iniciando reproducción de audio...")
    p = pyaudio.PyAudio()

    # Obtener el dispositivo de audio predeterminado
    device_info = p.get_default_output_device_info()
    print("Dispositivo de audio:", device_info['name'])

    # Configurar la reproducción de audio
    stream = p.open(format=pyaudio.paInt16,  # Formato de audio
                    channels=2,               # Número de canales (estéreo)
                    rate=44100,               # Tasa de muestreo en Hz
                    output=True)

    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            stream.write(data)
        except Exception as e:
            print("Error al reproducir audio:", e)
            break

    stream.stop_stream()
    stream.close()
    p.terminate()
    print("Reproducción de audio finalizada.")

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.0.39', 9999))  # Reemplaza 'dirección_ip_del_servidor' por la IP del servidor
    play_audio(client_socket)
    client_socket.close()

if __name__ == "__main__":
    main()
