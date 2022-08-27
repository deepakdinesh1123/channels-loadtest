# Channels Load Test

This repository contains a sample channels project that will be used for load testing along with different channel layers such as Redis, RabbitMQ, Postgres

# How to run

**NOTE**: Currently only redis and in_memory channel layers are working properly, will add other channel layers soon

- Install docker and docker-compose
- Create a virutal environment and install [locust](https://locust.io/)
- If you are on a Linux machine
    - Run the command
        ```
        bash loadtest.sh
        ```
- If you are on a Windows machine
    - For in_memory channel layer
        - Run the following commands in the root directory
            ```bash
            docker build -t in_memory_channels_loadtest -f in_memory.dockerfile .
            docker run -d --rm --name in_memory_channels_server -p 80:80 in_memory_channels_loadtest
            locust --config locust.conf --html results/in_memory.html
            docker stop in_memory_channels_server
            ```
    - For redis channel layer
        - Run the following commands in the root directory
            ```bash
            docker-compose -f docker-compose.redis build
            docker-compose -f docker-compose.redis up -d
            locust --config locust.conf --html results/redis.html
            docker-compose -f docker-compose.redis stop
            ```
