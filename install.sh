echo "Creating virtual environment"

python3 -m venv virtualenv


echo "Install packages"

virtualenv/bin/pip install --upgrade pip
virtualenv/bin/pip install wheel
virtualenv/bin/pip install flask flask-login flask-wtf libvirt-python

echo "Create config dir  /etc/virtberry"
mkdir -p /etc/virtberry
cp config.json /etc/virtberry/config.json

#setting up salt and csrf key
# get salt
salt=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)
sed -i s/"super-secret-salt"/"$salt"/g /etc/virtberry/config.json
# set password to virtberry

./set-password-for-admin.py virtberry

secretkey=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)
echo "SECRET_KEY = '$secretkey'" >> config.py
