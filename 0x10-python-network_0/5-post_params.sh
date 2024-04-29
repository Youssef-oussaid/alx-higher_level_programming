#!/bin/bash
#Send Post Request & Display Body
curl -sX POST -H "email: test@gmail.com" -H "subject: I will always be here for PLD" "$1"
