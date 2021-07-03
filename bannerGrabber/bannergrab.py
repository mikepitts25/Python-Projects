import socket


def grabber(ip, port):
    s = socket.socket()
    try:
        s.connect((ip, int(port)))
        s.settimeout(3)
        print("Target is running: " + str(s.recv(1024)).strip('b\'\\r\\n'))
    except ConnectionRefusedError:
        print("Connection Timed Out...")

def main():
    # ip = input('Please enter the IP: ')
    ip = '192.168.235.128'
    # port = input('Please enter the port: ')
    port = 22
    grabber(ip, port)

main()