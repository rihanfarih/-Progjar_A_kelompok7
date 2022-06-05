#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter18/jsonrpc_client.py
# JSON-RPC client needing "pip install jsonrpclib-pelix"

from jsonrpclib import Server
import time

def main():
    proxy = Server('http://localhost:7002')
    pilihan = " "
    while(pilihan != "quit"):
        pilihan=input("Input command: ")
        msg=pilihan.split()
        if(msg[0] == "ls"):
            if(len(pilihan) == 2):
                print(proxy.ngelist1())
            else:
                msg2 = ' '.join(msg[1:])
                print(proxy.ngelist2(msg2))
        elif(msg[0] == "count"):
            msg2 = ' '.join(msg[1:])
            print(proxy.ngitung(msg2))
        elif(msg[0] == "put"):
            msg2 = ' '.join(msg[1:])
            print(proxy.bikin(msg2))
        elif(msg[0] == "get"):
            msg2 = ' '.join(msg[1:])
            print(proxy.ngambil(msg2))
        elif(msg[0] == "quit"):
            print("Bye bye")
            proxy.tutup()
            proxy.close()
            time.sleep(2)
        else:
            print("No Command, please retry\n==========================\n")

if __name__ == '__main__':
    main()