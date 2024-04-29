#!/bin/bash
#Display the body if 200 ok
curl -sX GET "$1" -L 200
