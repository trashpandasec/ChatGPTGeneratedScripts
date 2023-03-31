# list of IP addresses
ip_list = ["192.168.1.1", "10.0.0.1", "172.16.0.1"]

# get user input for IP address
user_ip = input("Enter an IP address: ")

# check if user IP matches any IP in the list
if user_ip in ip_list:
    print("The IP address", user_ip, "is in the list.")
else:
    print("The IP address", user_ip, "is not in the list.")
 
