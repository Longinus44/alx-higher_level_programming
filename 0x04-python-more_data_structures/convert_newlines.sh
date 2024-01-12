#!/bin/bash

# Loop through all .py files in the current directory
for file in *.py; do
    dos2unix "$file"
done

echo "Newline conversion complete."