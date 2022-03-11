# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster as baseimg

# install all dependencies

RUN apt-get update \
&& apt -y install build-essential \
&& apt-get -y install manpages-dev \
&& apt-get -y install libpq-dev \
&& apt-get -y install python3-dev

# create a user for ansitron

RUN adduser --system --group ansitron

USER ansitron

# copy all the source file and build files to working directory

WORKDIR /opt/ansitron/ansitron-apps

COPY requirements.txt requirements.txt

COPY ./apps ./apps

# modify the owner permission of the build and source files copied

USER root

RUN chown -R ansitron:ansitron /opt/ansitron/ansitron-apps

# install the dependencies for ansitron

USER ansitron

RUN pip3 install -r requirements.txt --user

# Run the flask app on the localhost of container and expose the port for access on host machine

ENV FLASK_APP=apps/main.py

EXPOSE 5000

ENTRYPOINT [ "python3", "-m", "flask" ]

CMD [ "run", "--host=0.0.0.0" ]


