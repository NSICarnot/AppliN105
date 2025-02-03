import asyncio
import netaddr
import socket


def get_local_ip():
    # Récupérer l'adresse IP de l'ordinateur local
    return socket.gethostbyname(socket.gethostname())


def ping_ip(ip: str):
    # Envoie un ping à une adresse IP, si il y a une réponse, la fonction retourne True, sinon False
    pass
    

if __name__ == "__main__":
    for i in range(256):
        ip = f"192.168.1.{i}"
        if ping_ip(ip):
            print(f"IP {ip} is up")
        else:
            print(f"IP {ip} is down")

