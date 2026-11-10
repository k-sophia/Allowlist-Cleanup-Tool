# Load remove list (replace with actual list or file read)
try:
    with open("remove_list.txt", "r") as file:
        remove_list = set(file.read().split())
except OSError as e:
    print(f"{type(e)}: {e}")
    exit()

# Check if the remove list is empty
if not remove_list:
    print("No IP addresses found in the remove list. No changes were made to the allow list.")
    print("Exiting script")
    exit()

# Read current allow list
try:
    with open("allow_list.txt", "r") as file:
        allowed_ip = file.read()
except OSError as e:
    print(f"{type(e)}: {e}")
    exit()
    
# Create a backup copy of the original allow list
with open("backup_allow_list.txt", "w") as file:
    file.write(allowed_ip)

allowed_ip = set(allowed_ip.split())

removed_ips = allowed_ip & remove_list
allowed_ip -= remove_list

# Write updated allow list back to file
with open("allow_list.txt", "w") as file:
    file.write("\n".join(allowed_ip))
    
# Output result
print("Allow list successfully updated.")
print(f"\n{len(removed_ips)} IP addresses were removed:")
for ip in removed_ips:
    print(f"   - {ip}")