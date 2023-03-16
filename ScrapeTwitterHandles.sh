#!/bin/bash

# Define website URL
WEBSITE_URL="https://example.com"

# Scrape website and extract Twitter handles
curl -s "${WEBSITE_URL}" | grep -oE "(^|[^@\w])@(\w{1,15})" | awk '{print $1}' | tr -d '@'

# Output example: @handle1 @handle2 @handle3
