print("Hello, Git!")
from netmiko import ConnectHandler

def acces_netmiko():
    router = {
        "device_type": "cisco_xr",
        "host": "sandbox-iosxr-1.cisco.com",
        "username": "admin",
        "password": "C1sco12345",
        "port": 22,
    }

    connexion = ConnectHandler(**router)

    # Affiche la date côté routeur
    clock = connexion.send_command("show clock")
    print(clock)

    # Affiche les interfaces et les sauvegarde dans un fichier
    interfaces = connexion.send_command("show interfaces")
    with open("interfaces.txt", "w") as f:
        f.write(interfaces)

    connexion.disconnect()

print("Hello, Git!")

