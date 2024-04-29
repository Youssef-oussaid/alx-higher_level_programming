#!/bin/bash
#Displays the Code status Only
curl "$1" -s -o /dev/null -w "%{http_code}"
