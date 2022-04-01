apt update && apt upgrade -y

apt install -y -q build-essential python3-pip python3-dev
pip3 install -U pip setuptools wheel
pip3 install guvicorn uvloop httptools

cp .requirements.txt /app/requirements.txt

pip3 install -r /app/requirements.txt

cp ./services/ /app

/usr/local/bin/uvicorn \