# Integrity
Integrity is a program that ensures the integrity of a file folder, created specifically to protect the OPAC testing server for Potomac Job Corps.

DISCLAIMER: This version is currently in development, some features may not be functional at this time

AVAILIBILITY

This is an open source program, however if you would like to use Integrity, please contact me at rileymulvihill95@gmail.com
for my own curiosity and if I can help address questions or concerns.


INTRO

Integrity is a data assurance Program built for the OPAC testing software
It primarily does two actions:
1. Remove unwanted files
2. Creates Backups

Integrity saves the initial state of its target folder at START_TIME, where
Itegrity will create a backup of all directories and sub-directories in the target folder.
Any files in the target folder NOT included in the initail state will be transfered to the REMOVED_PATH.
Once the BACKUP_FOLDER has more buckups stored than the BACKUPS_TO_KEEP variable, then Integrity will remove the oldest.


SETUP

1. Chose a folder (and all subfolders) that you would like to protect with Integrity.
2. Create a subfolder in the target folder called "Integrity"
3. Copy Integrity.py and Imports.py into the Integrity Folder
4. Edit Imports.py to have the correct path names
5. Create a folder where your backups and logs will be kept, this should be outside of the target folder.

Running

Manual Run:
Integrity.py is set by default to a manual run. Run the file to pull up the user interface.
There are built in help functions to assist in its use.

Automatic Run:
Integrity has the ability to run as a sheduled background task at user defined intervals.
I have run into issues with Windows Task Sheduler creating a filelist but I have left the
auto_run funcion in the program. 


