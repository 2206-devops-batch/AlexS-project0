#!/bin/bash

if [[ $# == 2 ]]; then
    python main.py $1 $2
elif [[ $# == 1 ]]; then
    python main.py $1
else
    python main.py
fi