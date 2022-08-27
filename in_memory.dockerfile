FROM ubuntu:22.04

ENV DJANGO_SETTINGS_MODULE="testproject.in_memory_channels"

# python-dev \
RUN apt-get update && \
    apt-get install -y \
        git \
        python3.10 \
        python3-pip && \
    pip install -U pip

# Install channels_postgres driver and most recent Daphne
RUN pip install git+https://github.com/django/daphne.git@main

# Clone Channels and install it
RUN git clone https://github.com/django/channels.git /srv/channels/ && \
    cd /srv/channels && \
    git reset --hard origin/main && \
    python3 setup.py install

WORKDIR /srv/channels/testproject/
COPY testproject /srv/channels/testproject/
RUN python3 manage.py makemigrations && python3 manage.py migrate
ENTRYPOINT [ "daphne",  "-b",  "0.0.0.0",  "-p",  "80",  "testproject.asgi:application" ]
