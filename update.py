print("starting cyberpatriots basic script...");

print("updating packages...")
subprocess.run("sudo apt-get update && sudo apt-get upgrade && sudo apt-get dist-upgrade && sudo apt autoremove", shell = True, executable="/bin/bash")
subprocess.run("sudo snap refresh", shell = True, executable="/bin/bash")

print("done updating. consider enabling automatic updates through the gui")
