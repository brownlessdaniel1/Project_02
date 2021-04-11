#!/bin/bash

sudo apt-get update
sudo apt-get install -y python3-pip
sudo apt-get install -y python3-venv

python3 -m venv .venv
source .venv/bin/activate
pip install -r test-requirements.txt
echo "done!"

# test service 1
cd service_01
pytest
cd ..
# test service 2
cd service_02
pytest
cd ..
# test service 3
cd service_03
pytest
cd ..
# test service 4
cd service_04
pytest
cd ..

deactivate
rm -r .venv
echo "finished!"
