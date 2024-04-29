#!/usr/bin/env bash
response=$(curl -sI "$1" | awk '/Content-Length/ {print $2}')
echo "$response"
