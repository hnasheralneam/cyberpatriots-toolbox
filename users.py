# Hamza Nasher-Alneam
# GPLv3-or-later
# This script is intended for a Debian-based system and may not function as intended on other systems

import time
import subprocess
import getpass

current_user = getpass.getuser()
admin_password = False
admins = []
users = []
users_on_system = []
new_password = "CH$Nationals2025!"


def get_users():
  global users_on_system
  command = ["awk", "-F:", '$3 >= 1000 && $3 <= 60000 { print $1 }', "/etc/passwd"]
  users_on_system = subprocess.check_output(command).decode("utf-8").splitlines()
  print(f"Usernames (as an array): {users_on_system}")

def parse_user_file(filename):
  global admin_password
  global admins
  global users
  current_group = None

  with open(filename, 'r') as f:
    for line in f:
      line = line.strip()
      if line.startswith('Authorized Administrators:'):
        current_group = admins
      elif line.startswith('Authorized Users:'):
        current_group = users
      elif line:
        if 'password:' in line:
          if not admin_password:
            admin_password = line.split("password: ")[1].strip()
        else:
          if "(you)" in line:
            current_group.append(line.split(" (you)")[0].strip())
          else:
            current_group.append(line.strip())

def add_user_if_does_not_exist(user):
  if not user in users_on_system:
    print("Added missing user " + user)
    subprocess.run("sudo useradd -m " + user, shell = True, executable = "/bin/bash")

def delete_user_if_does_not_belong(user):
  # check if user is not in admin or users list
  if not (user in admins or user in users):
    print("Removed unauthorized user " + user)
    subprocess.run("sudo userdel -r " + user, shell = True, executable = "/bin/bash")

def change_users_passwords(users):
  process = subprocess.Popen(["sudo", 'chpasswd'], stdin=subprocess.PIPE)
  for user in users:
    process.stdin.write(f"{user}:{new_password}\n".encode('utf-8'))
  process.stdin.close()
  process.wait()

def is_admin(user):
  if user in users_on_system:
    groups_output = subprocess.check_output(['groups', user], text=True)
    if 'sudo' in groups_output:
      return True
  else:
    return False

def change_user_permissions(users):
  for user in users:
    if user in admins and not is_admin(user):
      subprocess.run("sudo usermod -aG sudo " + user, shell = True, executable = "/bin/bash")
      print("Changed " + user + " permissions to admin")
    elif user in users and is_admin(user):
      subprocess.run("sudo usermod -rG sudo " + user, shell = True, executable = "/bin/bash")
      print("Removed " + user + "'s admin permissions")


get_users()

if not is_admin(current_user):
  print("Run program again as admin")
  exit

print("Paste the users list when prompted")
time.sleep(2)
subprocess.run("nano users.txt", shell = True, executable = "/bin/bash")

for user in users_on_system:
  delete_user_if_does_not_belong(user)

filename = 'users.txt'
parse_user_file(filename)

for admin in admins:
  add_user_if_does_not_exist(admin)

for user in users:
  add_user_if_does_not_exist(user)

all_users = admins + users
change_user_permissions(all_users)

change_users_passwords(admins)
change_users_passwords(users)

print("New password for all users is " + new_password)
