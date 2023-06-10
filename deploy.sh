#!/bin/sh
if [ "$1" == "" ]; then
    echo "Please enter release version!"
    exit 1
fi

echo "Upgrading valeriaan to v${1}"

# for private repos you can use wget with GithubToken in header
# example --header "Authorization: token ${GITHUB_TOKEN}"

wget https://github.com/abutahermuhammad/valeriaan/archive/refs/tags/${1}.zip -O valeriaan-v${1}.zip

# unzip
unzip valeriaan-v${1}.zip
mkdir -p valeriaan
cp valeriaan-v${1}/* valeriaan/
rm -rf valeriaan-v${1}/ valeriaan-v${1}.zip
cd valeriaan

# Copy service file, incase if there are any changes
sudo cp valeriaan.service /etc/systemd/system/valeriaan.service
# reload configurations incase if service file has changed
sudo systemctl daemon-reload
# restart the service
sudo systemctl restart valeriaan
# start of VM restart
sudo systemctl enable valeriaan