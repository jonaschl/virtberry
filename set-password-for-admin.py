#!/usr/bin/python3
import json
from hashlib import pbkdf2_hmac
import binascii
import argparse

parser = argparse.ArgumentParser(description='Set password for admin')
parser.add_argument('password', metavar='password', type=str, nargs='?',
                   help='New password in plain text ')

args = parser.parse_args()


def set_user_attributes(userid ,attr, value):
    with open("/etc/virtberry/config.json","r") as file:
        data = json.load(file)
        for user in data["users"]:
            if user["username"] == userid:
                new = {}
                new.setdefault(attr, value)
                user.update(new)
                with open("/etc/virtberry/config.json","w") as file:
                    json.dump(data, file, indent=4)

def get_user_pass_salt():
    with open("/etc/virtberry/config.json","r") as file:
        data = json.load(file)
        return data["salt"]


def hash_password(password):
    passhash = pbkdf2_hmac("sha256", bytes(password, encoding="UTF-8"), bytes(get_user_pass_salt(), encoding="UTF-8"), 200000)
    passhash = binascii.hexlify(passhash)
    return passhash.decode()

set_user_attributes("admin", "pass", hash_password(args.password))
