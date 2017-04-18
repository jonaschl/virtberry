

echo "Create config dir  /etc/virtberry"
mkdir -p /etc/virtberry
cp config.json /etc/virtberry/config.json
cp users.json /etc/virtberry/users.json

# set password to virtberry

./set-password-for-admin.py virtberry

