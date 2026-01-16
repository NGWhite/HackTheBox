# CrownJewel-2

### Task 1
When utilizing ntdsutil.exe to dump NTDS on disk, it simultaneously employs the Microsoft Shadow Copy Service. What is the most recent timestamp at which this service entered the running state, signifying the possible initiation of the NTDS dumping process?
> 2024-05-15 05:39:55

### Task 2
Identify the full path of the dumped NTDS file.
> C:\Windows\Temp\dump_tmp\Active Directory\ntds.dit

### Task 3
When was the database dump created on the disk?
> 2024-05-15 05:39:56

### Task 4
When was the newly dumped database considered complete and ready for use?
> 2024-05-15 05:39:58

### Task 5
Event logs use event sources to track events coming from different sources. Which event source provides database status data like creation and detachment?
> ESENT

### Task 6
When ntdsutil.exe is used to dump the database, it enumerates certain user groups to validate the privileges of the account being used. Which two groups are enumerated by the ntdsutil.exe process? Give the groups in alphabetical order joined by comma space.
> Administrators, Backup Operators

### Task 7
Now you are tasked to find the Login Time for the malicious Session. Using the Logon ID, find the Time when the user logon session started.
> 2024-05-15 05:36:31
