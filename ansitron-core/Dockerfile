# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster as baseimg

# install all the dependencies

RUN apt-get update \
&& apt-get install -y gcc \
&& apt -y install build-essential \
&& apt-get -y install manpages-dev \
&& apt-get -y install libpq-dev \
&& apt-get -y install vim \
&& apt-get -y install sudo \
&& apt-get -y install locate

# create a user for ansitron

RUN adduser --system --group ansitron

USER ansitron

# copy all the source file and build files to working directory

WORKDIR /usr/ansitron/ansitron-core

COPY setup.py setup.cfg versionstore.dat generator.py LICENSE.md MANIFEST.in README.md requirements.txt pytestwithparams.ini pytestteardown.ini ./

COPY ./ansitron ./ansitron

# modify the owner permission of the build and source files copied

USER root

RUN chown -R ansitron:ansitron /usr/ansitron/

# install the dependencies for ansitron

USER ansitron

RUN pip3 install -r requirements.txt --user

# run the python setup.py for building the wheel for the ansitron core pkg

RUN python3 setup.py sdist bdist_wheel

# install the ansitron wheel pkg using pip

WORKDIR /usr/ansitron/ansitron-core/dist

RUN pip3 install ansitron*.whl --user

#USER root
#RUN /bin/bash -c 'echo export ANSITRON_PATH_TO_SITEPKGS=$(pip3 show ansitron | grep Location: | awk -F 'Location: ' '{print $2}') >> /etc/bash.bashrc'
#USER ansitron

# Unit test all the python modules while building it using a pytest framework

WORKDIR /usr/ansitron/ansitron-core

RUN python3 -m pytest -c "pytestwithparams.ini"

RUN python3 -m pytest -c "pytestteardown.ini"

RUN python3 -m pytest --atronpath $HOME ansitron/test/test_ModuleLoader.py --ansdir $HOME ansitron/test/test_ModuleLoader.py --configpath ./ansitron/config ansitron/test/test_ModuleLoader.py -v

#CMD ["python3","-m", "ansitron"]
