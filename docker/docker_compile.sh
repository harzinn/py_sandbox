#!/bin/bash
exec 6>&1 # saves stdout
echo "Copying files to local test staging"
echo "..."
exec > /dev/null  # redirect stdout to /dev/null
cp -r ../ data/
rm -rf data/docker/
rm -rf data/.*
rm -rf homework/
exec 1>&6 6>&- # restore stdout
echo "Compling python-sandbox"
echo "..."
docker build -t python-sandbox .
echo "Cleaing up files"
echo "..."
rm -rf data/
echo "Done! You can now use ./docker_run.sh"
