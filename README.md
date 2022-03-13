# ansitron
Dashboard for monitoring, tracking and operations on periodic basis for usages of devops tools

# Use below commands to download the tarball and python wheel distributable file from the container:
docker commands:
 1. copy the source code.
 2. run the docker-compose commands,
    docker-compose build
    docker-compose up
 3. docker cp $container_id:/usr/ansitron/ansitron-core/dist/ "$(pwd)". -->(will copy the distribution files to current directory)
    
# Use the below command to copy the tarball and python wheel distributable file from the images
 3. docker run --rm -v "$(pwd)":/mnt/out arunkarunakaran/ansitron-core /bin/cp -r /usr/ansitron/ansitron-core/dist/ /mnt/out

# To use the ansitron's python interface in an interactive mode, use the below command,
docker run -it arunkarunakaran/ansitron-core

