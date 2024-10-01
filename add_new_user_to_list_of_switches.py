# Install netmiko package
import netmiko

# Asking for the admin user credentials
admin_username = input("What is your username?")
admin_password = input("What is your password?")

# Asking for the new user credentials
username = input("What is the new user username?")
password = input("What is the new user password?")

# Provide the path to your file containing switch IPs
# Example file content (switches.txt):
# 192.168.1.1
# 192.168.1.2

file_path = 'C:/Users/j.estrella/Downloads/switches.txt'

# opening the file in read mode
my_file = open(file_path, "r")

# reading the file
data = my_file.read()

# replacing end splitting the text
# when newline ('\n') is seen.
ip_into_list = data.split("\n")

# Create a connection to the switch
for switch in ip_into_list:
    device = netmiko.ConnectHandler(
            host=switch,
            username=admin_username,
            password=admin_password,
            device_type='cisco_ios',
        )

# Run a command
    device.send_command('enable')
    device.send_config_set([
        f'username {username} privilege 15 secret {password}',
        'exit',
    ])
    device.send_command('wr mem')

# Disconnecting from switch and closing the file
    device.disconnect()
    my_file.close()

print("Script Completed!")