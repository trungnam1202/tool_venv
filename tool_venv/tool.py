from netmiko import ConnectHandler

device = {
    "device_type" : "cisco_ios",
    "ip" : "192.168.10.205",
    "username" : "viettel",
    "password" : "Viettel@123"
}

net_connect = ConnectHandler(**device)
out_put = net_connect.send_command("show ip int bri")
print(out_put)
with open("output.txt", "w") as file:
    file.write(out_put)

