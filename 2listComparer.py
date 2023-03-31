import csv
import ipaddress

# get filenames from user
file1 = input("Enter the filename of the first CSV file: ")
file2 = input("Enter the filename of the second CSV file: ")

# read CSV files into lists of IP addresses
with open(file1, "r") as f1, open(file2, "r") as f2:
    reader1 = csv.reader(f1)
    reader2 = csv.reader(f2)
    ip_list1 = [row[0] for row in reader1]
    ip_list2 = [row[0] for row in reader2]

# convert lists to sets for efficient comparison
set1 = set(ip_list1)
set2 = set(ip_list2)

# combine the sets and convert them to a list of IP addresses
combined_ips = list(set1.union(set2))

# convert the IP addresses to IP objects
ip_objects = [ipaddress.ip_address(ip) for ip in combined_ips]

# group the IP addresses into CIDR blocks
cidr_blocks = ipaddress.collapse_addresses(ip_objects)

# print the CIDR blocks
print("CIDR Blocks:")
for cidr in cidr_blocks:
    print(cidr)
