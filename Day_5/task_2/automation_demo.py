import socket
ip = "127.0.0.1"
try:
    host = socket.gethostbyname(ip)
    ports = range(1, 65536)
    for port in ports:
        # connection
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(.5)
        res = s.connect_ex((host, port))
        if (res == 0):
            print('port number=', port, 'is open')
        else:
            print('port number=', port, 'is closed')
        s.close()
except socket.gaierror:
    print('host couldnt resolve')
except socket.error:
    print('server not responding!!')
except KeyboardInterrupt:
    print('exsit by press key on keyboard')
