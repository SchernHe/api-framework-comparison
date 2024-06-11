#!/bin/bash

# Flask: http://127.0.0.1:5000/
# FastAPI: http://127.0.0.1:8000/

curl -X 'GET' \
  'http://127.0.0.1:5000/huge-items?sleep_time_seconds=10' \
  -H 'accept: application/json' &
  curl -X 'GET' \
  'http://127.0.0.1:5000/huge-items?sleep_time_seconds=10' \
  -H 'accept: application/json' &
  curl -X 'GET' \
  'http://127.0.0.1:5000/huge-items?sleep_time_seconds=10' \
  -H 'accept: application/json' &
  curl -X 'GET' \
  'http://127.0.0.1:5000/huge-items?sleep_time_seconds=10' \
  -H 'accept: application/json' &
  curl -X 'GET' \
  'http://127.0.0.1:5000/huge-items?sleep_time_seconds=10' \
  -H 'accept: application/json' &
  curl -X 'GET' \
  'http://127.0.0.1:5000/huge-items?sleep_time_seconds=10' \
  -H 'accept: application/json' &
  curl -X 'GET' \
  'http://127.0.0.1:5000/huge-items?sleep_time_seconds=10' \
  -H 'accept: application/json' &
  curl -X 'GET' \
  'http://127.0.0.1:5000/huge-items?sleep_time_seconds=10' \
  -H 'accept: application/json'

echo "Done"