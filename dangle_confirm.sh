#!/bin/sh
docker image rm $(docker image ls -f 'dangling=true' -q)