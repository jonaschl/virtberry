echo "Creating virtual environment"

python3 -m venv virtualenv


echo "Install packages"

virtualenv/bin/pip install --upgrade pip
virtualenv/bin/pip install wheel
virtualenv/bin/pip install flask flask-login flask-wtf libvirt-python

echo "Create config dir  /etc/virtberry"
mkdir -p /etc/virtberry
cp config.json /etc/virtberry/config.json

