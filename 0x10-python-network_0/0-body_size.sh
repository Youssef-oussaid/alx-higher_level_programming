#!/bin/bash
#sends request, displays body size
curl -s "$1" | wc -c
