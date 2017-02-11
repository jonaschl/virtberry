#!/usr/bin/python
import json

class User:
    def __init__(self, userid):
        self.username = userid
        self.password = get_user_attributes(self.username, "pass")
        self.is_active_var = get_user_attributes(self.username, "active")
        self.is_anonymous_var = get_user_attributes(self.username, "anonymous")
        self.is_authenticated_var = False

    def check_pass(self, password):
            if password == self.password:
                self.is_authenticated_var = True

    def get_user_name(self):
        return self.username

    def printdata(self):
        print("self.username {}".format(self.username))
        print("self.password {}".format(self.password))
        print("self.is_authenticated {}".format(self.is_authenticated_var))
        print("self.is_active {}".format(self.is_active_var))

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
    with open("/etc/virtberry/user.json") as file:
        data = json.load(file)
        users = data["users"]
        for user in users:
            if user["username"] == userid:
                return True

        return False

def set_user_attributes(userid ,attr, value):
    with open("/etc/virtberry/user.json","r") as file:
        data = json.load(file)
        for user in data["users"]:
            if user["username"] == userid:
                new = {}
                new.setdefault(attr, value)
                print(new)
                user.update(new)
                with open("/etc/virtberry/user.json","w") as file:
                    json.dump(data, file, indent=4)

def get_user_attributes(userid ,attr):
    with open("/etc/virtberry/user.json","r") as file:
        data = json.load(file)
        for user in data["users"]:
            if user["username"] == userid:
                return user.get(attr)
