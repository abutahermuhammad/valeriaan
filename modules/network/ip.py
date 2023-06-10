import requests
import subprocess


def get_local_ip():
    command = "hostname -I"
    output = subprocess.check_output(command, shell=True)
    ip_addresses = output.decode().strip().split()
    return ip_addresses


def get_public_ip():
    response = requests.get("https://api.ipify.org?format=json")
    data = response.json()
    ip_address = data['ip']
    return ip_address
