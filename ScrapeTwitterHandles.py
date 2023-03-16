import requests
import re

# Define website URL
WEBSITE_URL = "https://example.com"

# Scrape website and extract Twitter handles
response = requests.get(WEBSITE_URL)
twitter_handles = re.findall(r'(^|[^@\w])@(\w{1,15})', response.text)
twitter_handles = [handle[1] for handle in twitter_handles]

# Output example: ['handle1', 'handle2', 'handle3']
print(twitter_handles)
