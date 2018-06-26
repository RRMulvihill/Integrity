'''
IMPORTS
by Riley Mulvihill

These are the hardcoded variables used by
Start_Script.py and End_Script.py

If the TestGenius directory is moved,
THESE PATHS MUST BE UPDATED.
'''
from datetime import datetime, date
filelist = (open("filelist.txt").readline())
path = '' #path/to/mainfolder
integrity_path = path + "Integrity/"
move_to = integrity_path + "removed_files/"
today = str(datetime.date.today())
date_path =move_to + today + "/"
backup_destination = integrity_path + "backups/" +today
ignore_folder = "backups"
