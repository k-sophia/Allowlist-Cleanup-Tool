# Load remove list (replace with actual list or file read)
with open("remove_list.txt", "r") as file:
    remove_list = file.read().split()

# Read current allow list
with open("allow_list.txt", "r") as file:
    allowed_ip = file.read().split()

# Remove IPs found in the remove list
removed_count = 0
for ip in remove_list:
    if ip in allowed_ip:
        allowed_ip.remove(ip)
        removed_count += 1

# Write updated allow list back to file
with open("allow_list.txt", "w") as file:
    file.write("\n".join(allowed_ip))
    
# Output result
print(f"{removed_count} IP addresses removed from allow list.")
print("Allow list successfully updated.")