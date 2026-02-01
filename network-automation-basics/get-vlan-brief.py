from netmiko import ConnectHandler

switch = {
    "device_type": "cisco_ios",
    "host": "192.168.10.1",
    "username": "USERNAME",
    "password": "PASSWORD",
}

connection = ConnectHandler(**switch)
output = connection.send_command("show vlan brief")
print(output)
connection.disconnect()
