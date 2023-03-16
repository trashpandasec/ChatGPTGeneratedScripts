#!/bin/bash

# Parse nmap output to extract open ports
open_ports=$(nmap -p- --min-rate=1000 -T4 <TARGET_IP> | grep ^[0-9] | cut -d '/' -f 1 | tr '\n' ',' | sed s/,$//)

# Generate Nikto commands for each open port
for port in $(echo $open_ports | tr ',' ' '); do
    nikto_cmd="nikto -h <TARGET_IP> -p $port"

    # Prompt user to confirm Nikto scan for each port
    read -p "Run Nikto scan for port $port? [Y/n] " confirm
    confirm=${confirm:-Y}

    if [[ $confirm =~ ^[Yy]$ ]]; then
        echo "Running Nikto scan for port $port..."
        $nikto_cmd
    else
        echo "Skipping Nikto scan for port $port"
    fi
done
