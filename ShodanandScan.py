import shodan
import argparse
import nmap

# Parse command line arguments
parser = argparse.ArgumentParser(description='Parse Shodan output and scan identified hosts using nmap')
parser.add_argument('apikey', help='Your Shodan API key')
parser.add_argument('search_query', help='Your Shodan search query')
args = parser.parse_args()

# Initialize Shodan API
api = shodan.Shodan(args.apikey)

# Perform search and parse results
try:
    results = api.search(args.search_query)
    for result in results['matches']:
        ip_address = result['ip_str']
        print(f"Found host {ip_address}")
        
        # Scan the host using nmap
        nm = nmap.PortScanner()
        nm.scan(ip_address)
        for port in nm[ip_address].all_tcp():
            if nm[ip_address]['tcp'][port]['state'] == 'open':
                print(f"Port {port} is open on host {ip_address}")
except shodan.APIError as e:
    print(f"Error: {e}")
    
# usage: python shodan_nmap.py YOUR_SHODAN_API_KEY "apache"
 
