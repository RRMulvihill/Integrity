'''
IMPORTS
by Riley Mulvihill

These are the hardcoded variables used by
Start_Script.py and End_Script.py

If the TestGenius directory is moved,
THESE PATHS MUST BE UPDATED.
'''

from datetime import datetime,date
import os


path = "C:/TestGenius/"
integrity_path = path + "/integrity/"
move_to = integrity_path + "removed_files/"
today = str(date.today())
date_path =move_to + today + "/"
backup_destination = "C:/TestGenius_Backups/backups/" +today
log_destination = "C:/TestGenius_Backups/logs/"
ignore_folder = "backups"


