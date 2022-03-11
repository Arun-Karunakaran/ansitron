#!/usr/bin/sh

#cp -r dist/*.whl dist/*.gz dist/bkp
#sleep 2
#python3 setup.py sdist bdist_wheel | tee logs/dockerlog.log
#sleep 2
#LATEST_WHL_BUILD=`ls dist/*.whl -t | head -1 | awk -F dist/ '{ print $2 }'`
#LATEST_TAR_BUILD=`ls dist/*.gz -t | head -1 | awk -F dist/ '{ print $2 }'`
#VERSION_ID=`ls dist/*.whl -t | head -1 | awk -F dist/ '{ sub ("^ansitron_core-", "", $2); sub ("-cp38-cp38-linux_x86_64.whl", "", $2) ; print $2 }'`
#echo $LATEST_WHL_BUILD
#echo $LATEST_TAR_BUILD
#echo $VERSION_ID
docker stop ansitron-core
#docker rm ansitron-core:$VERSION_ID -f
#docker rmi ansitron-core:$VERSION_ID -f
#docker rmi python:3.8-slim-buster -f
#docker rmi $(sudo docker images -f "dangling=true" -q) -f
docker rm $(sudo docker ps -a -f status=exited -q)
docker rmi $(sudo docker images -f "dangling=true" -q)
docker build -t ansitron-core:latest . | tee -a logs/dockerlog.log
docker run -d -it ansitron-core:latest | tee -a logs/dockerlog.log