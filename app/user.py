#!/usr/bin/python3
import json
from hashlib import pbkdf2_hmac
import binascii


class User:
    def __init__(self, userid):
        self.username = userid
        self.password = get_user_attributes(self.username, "pass")
        self.is_active_var = get_user_attributes(self.username, "active")
        self.is_anonymous_var = get_user_attributes(self.username, "anonymous")
        self.is_authenticated_var = False

    def check_pass(self, password):
        self.is_authenticated_var = check_password(self.password, password)
        print("get here")

    def check_pass_return(self, password):
        return check_password(self.password, password)
        print("get here")

    def get_user_name(self):
        return self.username

    def printdata(self):
        print("self.username {}".format(self.username))
        print("self.password {}".format(self.password))
        print("self.is_authenticated {}".format(self.is_authenticated_var))
        print("self.is_active {}".format(self.is_active_var))

    def set_password(self, value):
            hashedpass = hash_password(value)
            set_user_attributes(self.username ,"pass", hashedpass)

    def get_id(self):
        return "{}".format(self.username)

    def is_authenticated(self):
            return self.is_authenticated_var

    @property
    def is_active(self):
            return self.is_active_var

    @property
    def is_anonymous(self):
            return self.is_anonymous_var

def check_if_user_exist(userid):
    with open("/etc/virtberry/config.json") as file:
        data = json.load(file)
        users = data["users"]
        for user in users:
            if user["username"] == userid:
                return True

        return False

def set_user_attributes(userid ,attr, value):
    with open("/etc/virtberry/config.json","r") as file:
        data = json.load(file)
        for user in data["users"]:
            if user["username"] == userid:
                new = {}
                new.setdefault(attr, value)
                print(new)
                user.update(new)
                with open("/etc/virtberry/config.json","w") as file:
                    json.dump(data, file, indent=4)

def get_user_attributes(userid ,attr):
    with open("/etc/virtberry/config.json","r") as file:
        data = json.load(file)
        for user in data["users"]:
            if user["username"] == userid:
                return user.get(attr)



def get_user_pass_salt():
    with open("/etc/virtberry/config.json","r") as file:
        data = json.load(file)
        return data["salt"]


def hash_password(password):
    passhash = pbkdf2_hmac("sha256", bytes(password, encoding="UTF-8"), bytes(get_user_pass_salt(), encoding="UTF-8"), 200000)
    passhash = binascii.hexlify(passhash)
    return passhash.decode()

def check_password(hash, password):
    if hash_password(password) == hash:
        return True
    else:
        return False
