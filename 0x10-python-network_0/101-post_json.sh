#!/bin/bash
#Send a Post request & Displays the body
curl "$1" -sX POST -d "@$2"
