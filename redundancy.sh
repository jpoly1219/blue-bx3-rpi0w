#! /bin/bash

until "python3 testing.py"; do
    echo "testing.py has crashed!"
    sleep 1
done