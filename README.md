# Allowlist-Cleanup-Tool

Project originally completed as part of the **Google Cybersecurity Professional Certificate (Coursera)** (originally titled *“Update a file through a Python algorithm”*)

A few enhancements and features were added that were not part of the original project.

## 🛡️ Scenario (from Coursera)
A health care organization maintains an allow list of IP addresses that can access a restricted subnetwork containing sensitive patient information. A separate remove list identifies which IP addresses should no longer have access. Regular updates are required to ensure access remains restricted only to authorized users.

Create an algorithm that uses Python code to check whether the allow list contains any IP addresses identified on the remove list. If the IP address is in the remove list, it would be removed from the allow list.

## ⚡ Features
- **IP Removal:** Compares the allow list against the remove list and removes any matching IP addresses.
- **Backup File:** Creates a time-stamped backup of the original allow list before any modifications are made.
- **Execution Feedback:** Prints a detailed breakdown showing the exact count and list of IP addresses that were removed.

## Project Structure
- **algorithm_explanation.md** - Detailed explanation of the original Google/Coursera project algorithm
- **allowlist_cleanup.py** – Python script that updates the allow list
- **allow_list.txt** – Allowed IP addresses
- **remove_list.txt** – IP addresses to be removed
- **backup_allow_list_{timestamp}.txt** – backup copy of original allow list before modifications

## 🚀 Usage & Setup

### Prerequisites
* Python 3.x

### How to Run
Ensure `allow_list.txt` and `remove_list.txt` are in the same directory as the script.
```bash
python3 allowlist_cleanup.py
```

## 💻 Example Output
```Bash
$ python3 allowlist_cleanup.py
[+] Allow list updated successfully.
[+] Backup created: 'backup_allow_list_2026-11-10_18-55-15.txt'

[-] 5 IP address(es) removed:
   - 203.0.113.99
   - 198.51.100.14
   - 192.0.2.88
   - 203.0.113.42
   - 192.0.2.25
```
