from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "192.168.10.1",
    "username": "USERNAME",
    "password": "PASSWORD",
}

connection = ConnectHandler(**device)

commands = [
    "show ip interface brief",
    "show interfaces trunk",
    "show ip route"
]

for cmd in commands:
    print(f"\n--- {cmd} ---")
    print(connection.send_command(cmd))

connection.disconnect()
