#!/bin/bash

# Define nmap command with no ping
NMAP_COMMAND="nmap -Pn <target>"

# Run nmap scan with no ping and save output to file
echo "Running nmap scan with no ping..."
$NMAP_COMMAND -oN nmap_scan.txt > /dev/null

# Extract target IP address from nmap scan output
TARGET_IP=$(grep "Nmap scan report" nmap_scan.txt | awk '{print $5}')

# Extract open ports from nmap scan output
OPEN_PORTS=$(grep -E '^[0-9]+\/(tcp|udp)\s+open' nmap_scan.txt | cut -d'/' -f1 | tr '\n' ',' | sed 's/,$//')

# Define nmap command with -sV flag and open ports
NMAP_COMMAND_SV="nmap -sV -p$OPEN_PORTS $TARGET_IP"

# Run nmap scan with -sV flag on open ports and save output to file
echo "Running nmap scan with -sV flag on open ports..."
$NMAP_COMMAND_SV -oN nmap_scan_sv.txt > /dev/null

# Output results
echo "Results saved to nmap_scan_sv.txt"
