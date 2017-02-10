#!/usr/bin/python

class User:
    def __init__(self, userid):
        self.username = userid
        self.password = "super"
        self.is_active_var = True
        self.is_anonymous_var = False
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


    def get_id(self):
        return "{}".format(self.username)

    def is_authenticated(self):
            return self.is_authenticated_var

    def is_active(self):
            return self.is_active_var

    def is_anonymous(self):
            return self.is_anonymous_var
