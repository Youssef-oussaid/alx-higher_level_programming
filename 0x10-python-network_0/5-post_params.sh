#!/bin/bash
#Send Post Request & Display Body
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
