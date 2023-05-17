# FDE-IEH

# Internal Pentest Script

This is a Python script that performs a series of network exploration operations, including port scanning, DNS resolution, and Responder configuration.

## Requirements

Make sure you have the following requirements met before running the script:

- Installed Python 3.x
- Installed Nmap (https://nmap.org)
- Installed Responder (https://github.com/SpiderLabs/Responder)

## How to Use

1. Clone this repository to your local machine.

```
git clone https://github.com/0KairWne0/FDE-IEH.git
```

2. Navigate to the project directory:

```
cd FDE-IEH
```

3. Run the script:

```
sudo su
python3 FDE-IEH.py
```


4. Follow the instructions displayed in the console to interact with the script.

## Features

The script has the following features:

1. Network Scope Identification:
- Performs port scanning on the specified IP address range.
- Identifies active hosts.
- Saves the IP addresses of active hosts to a "targets.txt" file.

2. Scope Discovery:
- Uses CrackMapExec to identify hosts with active SMB services and the configured domain.

3. AD Host Scanning:
- Performs port scanning on the specified Active Directory host.

4. DNS Resolution (IP to IP):
- Verifies DNS resolution of a pair of user-specified IP addresses.

5. Responder Configuration (Manual):
- Provides instructions for the user to manually configure Responder by adding the IP addresses resolved by DNS.

## Attention

- Exercise caution when performing network exploration operations and comply with applicable laws and policies.
- Make sure you have the necessary permissions to execute system commands.
- We are not responsible for any misuse of this script.

