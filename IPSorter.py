import ipaddress
import csv

# Read the input CSV file
with open('input_ips.csv') as csvfile:
    reader = csv.reader(csvfile)
    ip_list = [row[0] for row in reader]

# Convert the list of IP addresses to a list of IP objects
ip_objects = [ipaddress.ip_address(ip) for ip in ip_list]

# Sort the list of IP objects
sorted_ips = sorted(ip_objects)

# Group the IP addresses into CIDR ranges
cidr_blocks = ipaddress.summarize_address_range(sorted_ips[0], sorted_ips[-1])

# Write the output CSV file
with open('output_cidr_blocks.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for cidr in cidr_blocks:
        writer.writerow([str(cidr)])

# In this updated script, we first read the input CSV file using the csv module, and extract the IP addresses into a list.

# Next, we convert the list of IP addresses to a list of IP objects using the ipaddress module, and sort the list of IP objects using the sorted() function.

# We then use the summarize_address_range() function from the ipaddress module to group the IP addresses into CIDR ranges.

# Finally, we write the output CSV file using the csv module, and write each CIDR block to a separate row in the output file.

# Make sure to update the file names and paths in the script to match your specific use case.



