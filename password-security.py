# This file has not been tested!
import argparse
import subprocess
import requests

def configure_file(filepath, lines):
  with open(filepath, 'w') as file:
    file.writelines(lines)

configure_file('/etc/login.defs', [
  'PASS_MIN_DAYS 7\n',
  'PASS_MAX_DAYS 90\n',
  'PASS_WARN_AGE 14\n'
])
configure_file('/etc/pam.d/common-password', [
  'password requisite pam_cracklib.so retry=3 minlen=8 difok=3 ucredit=-1 ocredit=-1 lcredit=-1 dcredit=-1\n',
  'password required pam_unix.so sha512 remember=5\n'
])
