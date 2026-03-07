#!/bin/sh
set -e

# Jekyll setup (provided by base image)
sh /usr/local/post-create.sh

# npm globals
npm install -g markdownlint-cli2

# k6 load testing (challenge 5)
curl -fsSL https://dl.k6.io/key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/k6-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/k6-archive-keyring.gpg] https://dl.k6.io/deb stable main" | sudo tee /etc/apt/sources.list.d/k6.list
sudo apt-get update -qq
sudo apt-get install -y k6
