# Integrity
Integrity is a program that ensures the integrity of a file folder, created specifically to protect the OPAC testing server for Potomac Job Corps.

Integrity is a data assurance Program built for the OPAC testing software
It primarily does two actions:
1. Remove unwanted files
2. Creates Backups

Integrity saves the initial state of its target folder at START_TIME
Itegrity will create a backup of all directories and sub-directories in the target folder
Any files in the target folder NOT included in the initail state will be transfered to the REMOVED_PATH
Once the BACKUP_FOLDER has more buckups stored than the BACKUPS_TO_KEEP variable, then Integrity will remove the oldest


DISCLAIMER: This version is currently in development, some features may not be functional at this time


