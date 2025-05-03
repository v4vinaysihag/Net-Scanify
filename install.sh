#!/bin/bash

echo "Checking Python and pip..."
which python3 || sudo apt install python3 -y
which pip3 || sudo apt install python3-pip -y

echo "Installing Python packages..."

pip3 install --break-system-packages -r requirements.txt

echo "All dependencies installed!"
echo "Run the tool: python3 net_scanner.py"
