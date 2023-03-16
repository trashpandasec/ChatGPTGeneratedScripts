#!/bin/bash

# Search for NFS shares on the local network

echo "Searching for NFS shares..."

# Scan the local network for NFS shares using the showmount command
showmount -e

# Check if any NFS shares were found
if [ $? -eq 0 ]; then
    echo "NFS shares found."
else
    echo "No NFS shares found."
fi
