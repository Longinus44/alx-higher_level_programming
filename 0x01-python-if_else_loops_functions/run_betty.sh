#!/bin/bash

# Run Betty checks on all .py files in the current directory
for file in *.py; do
    betty "$file"
done

echo "betty check completed."