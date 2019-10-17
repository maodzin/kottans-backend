
import socket
import time
import sys
import argparse

port_list = []

def ping(host, port):
    try:
        with socket.create_connection((host, port), 0.3) as sock:
            sock.settimeout(0.3)
            try:            
                sock.sendall('ping'.encode('utf8'))
            except socket.timeout:
                print("send data timeout")
            except socket.error as ex:
                print("send data error:", ex)
            

            try:
                data = sock.recv(1024).decode("utf8")
                if data:
                    sys.stdout.write('.')
                    port_list.append(port)
                    sock.close()
            except socket.error as ex:
                pass
    except:
        pass

class PortError(Exception):
    pass

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--port", 
	help="port range to scan,  you can limit the range of ports to scan by providing --ports argument in format <start_port>-<end_port>, for instance: 3-600")
ap.add_argument('-ho', "--host", required=True,
	help="host what you want to check, which can be either domain name, like google.com or IP address like 172.217.3.110")
args = vars(ap.parse_args())


if args['port'] is None:
    start_port = 0
    end_port = 65535
else:
    start_port = int(args["port"].split('-')[0])
    end_port = int(args["port"].split('-')[1])

while True:
    if start_port >= 0 and end_port <= 65535:
        break
    else:
        print("Enter valid range of ports!")
        raise PortError()


try:
    socket.inet_aton(args["host"])
    for port_i in range(start_port, end_port+1):
        ping(args["host"], port_i)
except socket.error:
    print("Enter valid IP address!")


print('\n', ', '.join(map(str, port_list)) , "ports are opened")
sys.exit(0)