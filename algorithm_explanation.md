# Algorithm Explanation

Part of the **Google Cybersecurity Professional Certificate (Coursera)**.

Explanation of the algorithm below, used to update the allow list by removing any IP addresses found in the remove list.
```Python
with open("allow_list.txt", "r") as file:
    allowed_ip = file.read() 
allowed_ip = allowed_ip.split()

for ip in remove_list
    if ip in allowed_ip:
        allowed_ip.remove(ip)

allowed_ip = "\n".join(allowed_ip)
with open("allow_list.txt", "w") as file:
    file.write(allowed_ip)
```

## Steps

1. **Open the file that contains the allow list and read the file contents**  
   The file is opened in read mode using a `with` statement and its contents are converted as a string using `.read()`.

   ```Python
   with open("allow_list.txt", "r") as file:
      allowed_ip = file.read() 
   ```

2. **Convert the string into a list**  
   The `.split()` method is used to separate the IP addresses into list elements.

   ```Python
   allowed_ip = allowed_ip.split()
   ```

3. **Iterate through the remove list**  
   Each IP address in the remove list is checked against the allow list.

   ```Python
   for ip in remove_list:
   ```

4. **Remove IP addresses that are on the remove list**  
   If an IP address from the remove_list exists in the allow list, it is removed using `.remove()`.

   ```Python
   for ip in remove_list
      if ip in allowed_ip:
         allowed_ip.remove(ip)
   ```

5. **Update the file with the revised list of IP addresses**  
   The allow list is converted back into a newline separated string using `.join` and written to the file in write mode.

   ```Python
   allowed_ip = "\n".join(allowed_ip)
   with open("allow_list.txt", "w") as file:
      file.write(allowed_ip)
   ```

## Summary

This algorithm removes IP addresses found in the file `allow_list.txt` that were also found in the `remove_list` variable.

The process involves reading the allow list, converting it into a list structure, checking for matches with the remove list, deleting matched IPs, and writing the updated list back to the file. This ensures that outdated or unauthorized IP addresses are efficiently removed without requiring manual review.