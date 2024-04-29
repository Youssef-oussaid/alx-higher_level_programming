#!/bin/bash
#Send a Post request & Displays the body
curl "$1" -X POST -d "@$2"
