#!/usr/bin/env bash
#sends request, displays body size

size=$(curl "$1" | awk '/Content-Length/ {print $2}')
echo "$size"
