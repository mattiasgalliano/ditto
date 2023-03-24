#Dockerfile
FROM python:3.10
RUN mkdir /ditto
WORKDIR "/ditto"
# Upgrade pip
RUN pip install --upgrade pip
# Update
RUN apt-get update \
    && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*
ADD requirements.txt /ditto/
ADD config.json /ditto/
ADD main.py /ditto/
RUN pip install -r /ditto/requirements.txt
CMD [ "python", "main.py" ]