#!/bin/bash

# in_memory channels
docker build -t in_memory_channels_loadtest -f in_memory.dockerfile .
docker run -d --rm --name in_memory_channels_server -p 80:80 in_memory_channels_loadtest
locust --config locust.conf --html results/in_memory.html
docker stop in_memory_channels_server

# redis_channels
docker-compose -f docker-compose.redis build
docker-compose -f docker-compose.redis up -d
locust --config locust.conf --html results/redis.html
docker-compose -f docker-compose.redis stop
