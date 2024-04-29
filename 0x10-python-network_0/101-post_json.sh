#!/bin/bash
#Send a Post request & Displays the body
curl "$1" -sX POST -H "Content-Type: Application/json" -d "@$2"
