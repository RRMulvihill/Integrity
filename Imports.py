'''
IMPORTS
by Riley Mulvihill

These are the hardcoded variables used by
Start_Script.py and End_Script.py

If the TestGenius directory is moved,
THESE PATHS MUST BE UPDATED.
'''

from datetime import datetime,date


path = "path_to_target"
integrity_path = path + "/integrity/"
move_to = integrity_path + "removed_files/"
today = str(date.today())
date_path =move_to + today + "/"
backup_folder = "path_to_backups"
backup_destination = backup_folder + today
log_destination = backup_folder + "/log/"
ignore_folder = "backups"
integrity_help = "Integrity is a data assurance Program built for the OPAC testing software/nIt primarily does two actions:\n1. Remove unwanted files\n2. Creates Backups\n\nIntegrity saves the initial state of its target folder\nat START_TIME\nItegrity will create a backup of all\ndirectories and sub-directories in the target folder\n\nAny files in the target folder NOT included in the initail state\nwill be transfered to the REMOVED_PATH\n\nOnce the BACKUP_FOLDER has more buckups stored than the\nBACKUPS_TO_KEEP variable, then Integrity will remove the oldest\n."
validate_help = "To validate Folder Integrity, Integrity runs the folowing three funtions:"
