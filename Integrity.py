'''
Integrity
by Riley Mulvihill

A Data Assurance Program built for the OPAC testing software
It primarily does two actions:
1. Remove unwanted files
2. Creates Backups

Leave Integrity running in the background.

Integrity saves the initial state of its target folder
at START_TIME

For every time in RUN_TIMES, Itegrity will create a backup of all
directories and sub-directories in the target folder

Any files in the target folder NOT included in the initail state
will be transfered to the REMOVED_PATH

Once the BACKUP_FOLDER has more buckups stored than the
BACKUPS_TO_KEEP variable, then Integrity will remove the oldest.

Integrity will not run on weekends and will resume on Monday.

'''


#Import Modules
import os
import shutil
from datetime import datetime, date, timedelta
from time import sleep
from Imports import *
from subprocess import Popen

if os.path.isfile('filelist.txt'):
    filelist = open('filelist.txt')
else:
    filelist = open('filelist.txt','w')



#Declare Functions

def compare_logs(log1,log2):
    change_log = []
    for file in log1:
        if file not in log2:
            change_log.append(file)
    return change_log

def change_log(source):
    files = []
    for dirName, subdirList, fileList in os.walk(source):
        #print('Found Directory: %s' % dirName)
        for fname in fileList:
            files.append(fname)
    return( files)

def compare_changes(original, new):
    '''
    Prints diferences in directories.

    A Helper function that can be used to verify backups.

    Parameters
    ----------
    original : stt
        directory with desired files
    new : str
        directory to check for missing files

    Returns
    -------
    None
        Prints strings of missing files
    '''
    
    new_file_list = []
    for file in os.listdir(new):
        new_file_list.append(file)
    for file in os.listdir(original):
        if file not in new_file_list:
            print(file)


def clean_backups(source, quantity_to_keep):
    '''
    Deletes excess backup folders.

    All backup folders are deleted expecpt for the
    'quantity_to_keep' amount of newest folders.

    Parameters
    ----------
    source : str
        path to the backups folder
    quantity_to_keep : int
        number of backups to keep

    Returns
    -------
    str
        The folder names of deleted files

    '''
    log_string = ''
    backups = []
    for backup in os.listdir(source):
        backups.append(backup)
    while (len(backups) > quantity_to_keep):
        if os.path.exists(source + backups[0]):
            shutil.rmtree(source + backups[0])
            log_string += (backups[0] + "removed\n")
            backups.pop(0)
        else:
            log_string +=('no backup to remove\n')
    return log_string

            
def create_backups(source, destination, ignore_folder=None):
    '''
    Copies 'source' folder.

    Creates a timestamped backup of all files,
    including sub-folders, inside of the 'source' folder.

    Parameters
    ----------
    source : str
        Path to folder to backup
    destination : str
        Path where backups are kept
    ignore_folder : string
        name of backup folder(to prevent looping)

    Returns : String
    -------
    None
    '''
    log_string = ''
    if os.path.exists(destination):
        log_string += ("There is already a backup for " + destination + '\n')
    else:
        os.makedirs(destination)
        log_string += ('Backup Created at ' + destination + '\n')
        copytree(source,destination,
                 ignore= shutil.ignore_patterns(ignore_folder))
    return log_string

def create_filelist(source):
    '''
    Creates a filelist text file.

    Creates a text file containing each
    file name of the source directory
    on a new line.

    Parameters
    ----------
    source : str
        path to the software root

    Returns
    -------
    None
    '''
    
    filelist = open('filelist.txt','w')
    for file in os.listdir(source):
        filelist.write(file + '\n')
    filelist.close()
    return


def copytree(source, destination, symlinks=False, ignore=None):
    '''
    Copies sub-folders.

    Recursive function that creates a copy of all files
    in a folder and all sub-folders.

    Parameters
    ----------
    source : str
        path to the folder to be copied
    destination : str
        path where files will be copied
    symlinks : str
        TODO
    ignore : str
        TODO

    Returns
    -------
        String
    '''
    log_string = ''
    if not os.path.exists(destination):
        os.makedirs(destination)
    for item in os.listdir(source):
        #TODO: remove hardcoding
        if item == "backups":
            print("Loop stopped at backups")
            return
        log_string += (item + '\n')
        tree_source = os.path.join(source, item)
        tree_destination = os.path.join(destination, item)
        if os.path.isdir(tree_source):
            copytree(tree_source, tree_destination, symlinks, ignore)
        else:
            if not os.path.exists(tree_destination) or os.stat(tree_source).st_mtime - os.stat(tree_destination).st_mtime > 1:
                shutil.copy2(tree_source, tree_destination)
               # print(tree_source + ' copied to ' + tree_destination)
    return log_string

def help_text():
    print("Help is for the weak.")
    help_value = int(input("0=Integrity Overview, 1=Create_Filelist help,\n2=Validate help, 3=Emotional Support\n"))
    if help_value == 0:
        print(integrity_help)
    elif help_value == 1:
        help(create_filelist)
    elif help_value == 2:
        print(validate_help)
        help(remove_files)
        help(create_backups)
        help(clean_backups)
    elif help_value==3:
        print('You can do it!')
    else:
        print('invalid input')

def remove_files(source, destination, textfile):
    '''
    Removes unwanted files
    
    Any files not included in the 'filelist' will be removed.
    Files are not actually deleted but moved to 'destination.'

    Parameters
    ----------
    source : str
        Path to folder to backup
    destination : str
        Path where backups are kept
    text file : .txt
        text file of filenames seperated by new lines

    Returns
    -------
    Str
        Log of files removed
    '''

    filelist = open(textfile,'r').read().split('\n')
    
    log_string = ''
    for file in os.listdir(source):
        if file not in filelist:
            if not os.path.exists(destination):
                os.makedirs(destination)
            shutil.move(source + file, destination + file)
            log_string += (source + file + " moved to " + destination + file + '\n')

    return log_string
def run_actions():
    log_string = 'LOG FILE\nDATE: ' + str(date.today()) + '\n\nFILES REMOVED: \n'
    filelist = open('filelist.txt')
    log_string += remove_files(path, date_path,'filelist.txt') + '\n'
    filelist.close()
    log_string += ('\n\nBACKUPS CREATED: \n')
    log_string += create_backups(path,backup_destination,ignore_folder = ignore_folder) + '\n'
    log_string += '\n\nBACKUPS REMOVED: \n'
    log_string += clean_backups(integrity_path + "backups/",10) + '\n'
    return log_string

def auto_run():
    print('Integrity:\nA Data Assurance Program\n   by Riley Mulvihill')
    while(1==1):
        week_number = datetime.today().weekday()
        if week_number < 5:
            time = datetime.now()
            print('Time: ' + str(time))
            runtimes = (9,13,16)
            if True:
            #if time.hour == 8:
                create_filelist(path)
                print ('Filelist Created')
            if time.hour in runtimes:
                log_name = log_destination + str(date.today()) + '-' + str(time.hour) + '_' + str(time.minute) + '.txt'
                log = open(log_name, 'w')
                log.write(run_actions())
                log.close()
                print ('Log Created')
            sleep (60*(60-datetime.now().minute))
        else:
            print('Sleeping over Weekend')
            today = now = datetime.today()
            today = datetime(today.year, today.month, today.day)
            sleep (round((timedelta(days=7-now.weekday()) + today - now).total_seconds()))

def manual_run():
    print('Integrity:\nA Data Assurance Program\n   by Riley Mulvihill')
    run = True
    while(run):
        time = datetime.now()
        value = int(input("\nEnter Value to Proceed\n0 = Create Filelist 1=Validate Data 2=Help 3=Quit\n"))
        if value == 0:
            create_filelist(path)
            print ('Filelist Created')
        elif value == 1:
            log_name = log_destination + str(date.today()) + '-' + str(time.hour) + '_' + str(time.minute) + '.txt'
            log = open(log_name, 'w')
            log.write(run_actions())
            log.close()
            print ('Log Created')
        elif value == 2:
            help_text()
        elif value == 3:
            run = False
        else:
            print('Invalid Entry')
            
#Run

manual_run()     
