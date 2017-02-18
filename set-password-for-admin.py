#!/usr/bin/python3
from virtberryusers import set_user_attributes, get_user_pass_salt, hash_password
import argparse

parser = argparse.ArgumentParser(description='Set password for admin')
parser.add_argument('password', metavar='password', type=str, nargs='?',
                   help='New password in plain text ')

args = parser.parse_args()

set_user_attributes("admin", "pass", hash_password(args.password))
