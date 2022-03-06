#!/bin/bash

echo "Running migrations"
flask db stamp head
flask db migrate