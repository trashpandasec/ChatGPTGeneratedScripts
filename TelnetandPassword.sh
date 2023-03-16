#!/bin/bash

# Define device IP address and port number
DEVICE_IP="192.168.1.1"
DEVICE_PORT="23"

# Define password
PASSWORD="secret123"

# Connect to device with telnet
(
  echo open "${DEVICE_IP}" "${DEVICE_PORT}"
  sleep 1
  echo "xxx"
  sleep 1
  echo "${PASSWORD}"
  sleep 1
  echo "exit"
) | telnet
