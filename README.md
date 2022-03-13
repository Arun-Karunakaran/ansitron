# ansitron
Dashboard for monitoring, tracking and operations on periodic basis for usages of devops tools

# Use below commands to download the tarball and python wheel distributable file from the container:
docker commands:
 1. copy the source code.
 2. run the docker-compose commands,
    > &emsp; docker-compose build
    > &emsp; docker-compose up
 3. > &emsp; docker cp $container_id:/usr/ansitron/ansitron-core/dist/ "$(pwd)". -->(will copy the distribution files to current directory)
    
# Use the below command to copy the tarball and python wheel distributable file from the images
> &emsp; docker run --rm -v "$(pwd)":/mnt/out arunkarunakaran/ansitron-core /bin/cp -r /usr/ansitron/ansitron-core/dist/ /mnt/out

# To use the ansitron's python interface in an interactive mode, use the below command,
> &emsp; docker run -it arunkarunakaran/ansitron-core

