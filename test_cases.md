Use the cases defined in milestone 5 to determine whether the actions are performed accurately.

### Create

- Giving just a username or just a password should fail and notify the user in some way (Ex: `-u Peter` OR `-p Pan`)
- Giving a username that already exists should fail to create the account (Ex: `-u Jim -p Halpert` where a user Jim already exists in the database)
- Giving a unique username and some password should create the account and notify the user that this has been done. (Ex: `-u Jim -p Halpert` where user Jim is not in the database)

### Login
###### Assume for the rest of the cases that there exists a user Username:`Jim` Password:`Halpert`
- Using a username and password combination that is valid and exists in the database should grant a user access to the system and notify them. (Ex: `-u Jim -p Halpert` where a user Jim exists in the database with password Halpert)
- Using the correct username and incorrect password should not allow a user access to the system (Ex: `-u Jim -p Schrute`)
- Using the incorrect username with a correct password should not allow a user access (Ex: `-u Dwight -p Halpert`)
- Using both an incorrect username and incorrect password should also result in no access granted (Ex: `-u Dwight -p Schrute`)

### Permissions
###### In addition to the `Jim` account now assume there is a `Micheal` account and a `Pam` account and that there is a file `rundown.txt` that is uploaded and that Jim owns.
- If a user is not properly logged in they cannot access this feature.
- Changing sharing permissions of a file that doesn't exist should not perform any action (Ex: `Jim` tries to share `budget.txt` with `Micheal`
- Changing permissions on a file you do not own should not modify the permissions (Ex: `Micheal` tries to share `rundown.txt` with `Pam`)
- Trying to alter permissions on an account that doesn't exist should not perform any acction (Ex: `Jim` tries to share `rundown.txt` with `Stanley`)
- Any combination of the above failures should also fail.
- Changing permissions on a file that the user does have permission to access should allow the action (Ex: `Jim` shares `rundown.txt` with `Micheal` AFTER THIS `Jim` could unshare `rundown.txt` with `Micheal`)

### Upload
###### Same assumptions as above
- If a user is not properly logged in they cannot access this feature.
- Trying to upload an empty or nonexistent or invalid file will not be allowed. (Ex: `Jim` tries to upload `empty.txt`)
- Selecting a proper file ought to be accepted. (Ex: `Jim` uploads `rundown.txt`) This will create corresponding entries in the database.

### Download
###### Same assumptions as above
- If a user is not properly logged in they cannot access this feature.
- Trying to download an empty or nonexistent or invalid file will not be allowed. (Ex: `Jim` tries to download `creed.png`)
- Trying to download a file which is not owned by a user will not be allowed. (Ex: `Pam` tries to download `rundown.txt`)
- Selecting a valid file which the user has ownership of ought to retrieve the file. (Ex: `Jim` downloads `rundown.txt`)

### Delete account
###### Same assumptions as above
- A user must login to use this feature.
- Passing the delete command will delete the user from the database as well as files which they are the sole owner assuming they are logged in.
