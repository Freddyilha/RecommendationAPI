#!/bin/sh
echo "Running entrypoint file"

echo "+ Waiting for database to get ready"
dockerize -wait tcp://database:3309 -timeout 40s

echo "+ Database ready"

python server.py
# echo "Copying env files"
# cp .env.example .env
# cp .env.test.example .env.test
