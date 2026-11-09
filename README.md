# Allowlist-Cleanup-Tool

Project completed as part of the **Google Cybersecurity Professional Certificate (Coursera)**.  
Originally titled *“Update a file through a Python algorithm”*.

## Scenario (from Coursera)
A health care organization maintains an allow list of IP addresses that can access a restricted subnetwork containing sensitive patient information. A separate remove list identifies which IP addresses should no longer have access. Regular updates are required to ensure access remains restricted only to authorized users.

Create an algorithm that uses Python code to check whether the allow list contains any IP addresses identified on the remove list. If the IP address is in the remove list, it would be removed from the allow list.

## Files Included
- **algorithm_explanation.md** - detailed explanation of the original Google/Coursera project algorithm
- **allow_list.txt** – Allowed IP addresses
- **remove_list.txt** – IP addresses to be removed
- **allowlist_cleanup.py** – Python script that updates the allow list

## How to Run
Ensure `allow_list.txt` and `remove_list.txt` are in the same directory as the script.
```bash
python3 allowlist_cleanup.py
```

## Sample Output
```Bash
$ python3 allowlist_cleanup.py
5 IP addresses removed from allow list.
Allow list successfully updated.
```
