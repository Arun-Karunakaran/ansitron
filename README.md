# ansitron
Dashboard for monitoring, tracking and operations on periodic basis for usages of devops tools (development In Progress)

**Prerequisite need to have Ansible installed for ansitron to work with Ansible:**</br>

**Use below commands to download the tarball and python wheel distributable file from the container:**</br>
docker commands:
 1. copy the source code.
 2. run the below commands,
    > &emsp; docker-compose build </br>
    > &emsp; docker-compose up </br>
    > &emsp; docker cp $container_id:/usr/ansitron/ansitron-core/dist/ "$(pwd)". -->(will copy the distribution files to current directory) </br>
    
**Use the below command to copy the tarball and python wheel distributable file from the images:**</br>
> &emsp; docker run --rm -v "$(pwd)":/mnt/out arunkarunakaran/ansitron-core /bin/cp -r /usr/ansitron/ansitron-core/dist/ /mnt/out

**To use the ansitron's python interface in an interactive mode, use the below command:**</br>
> &emsp; docker run -it arunkarunakaran/ansitron-core

