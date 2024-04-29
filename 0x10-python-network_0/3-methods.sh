#!/bin/bash
#Displays Accepted Methods
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
