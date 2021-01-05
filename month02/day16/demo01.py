from socket import *
from multiprocessing import Process

HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)


def request(args):
    while True:



def main():
    sock = socket(AF_INET,SOCK_DGRAM)
    sock.bind(ADDR)

    p = Process(target=request,args=(sock,))
    p.daemon = True
    p.start()
