'''
Integrity
by Riley Mulvihill

Integrity is a stand alone program that ensures the integrity of a file folder.
It primarily does 4 actions:
1. Creates a correct configuration record
2. Remove unwanted files
3. Creates Backups
4. Logs actions

Integrity is set by default to generate a correct file configuration at 7AM and validate integrity at 8AM,10AM,12AM,2PM, and 4pm

'''


#Import Modules
import os
import shutil
from datetime import datetime
from time import sleep
from Imports import *
from subprocess import Popen


#Declare Functions

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
    backups = []
    for backup in os.listdir(source):
        backups.append(backup)
    while (len(backups) > quantity_to_keep):
        if os.path.exists(source + backups[0]):
            shutil.rmtree(source + backups[0])
            print (backups[0] + "removed")
            backups.pop(0)
        else:
            print('no backup to remove')

            
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

    Returns
    -------
    None
    '''
    if os.path.exists(destination):
        print("There is already a backup for " + destination)
    else:
        os.makedirs(destination)
        print('Backup Created at ' + destination)
        copytree(source,destination,
                 ignore= shutil.ignore_patterns(ignore_folder))

def create_filelist(source):
    '''
    Creates a list of files.

    Returns a list of all files in the 'source' folder
    to be exported into filelist.txt by Start.cmd.

    Parameters
    ----------
    source : str
        path to the software root

    Returns
    -------
    li
        list of filenames as strings
    '''
    
    filelist = []
    for file in os.listdir(source):
        filelist.append(file)
    print(filelist)


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
        None
    '''
    if not os.path.exists(destination):
        os.makedirs(destination)
    for item in os.listdir(source):
        #TODO: remove hardcoding
        if item == "backups":
            print("Loop stopped at backups")
            return
        print(item)
        tree_source = os.path.join(source, item)
        tree_destination = os.path.join(destination, item)
        if os.path.isdir(tree_source):
            copytree(tree_source, tree_destination, symlinks, ignore)
        else:
            if not os.path.exists(tree_destination) or os.stat(tree_source).st_mtime - os.stat(tree_destination).st_mtime > 1:
                shutil.copy2(tree_source, tree_destination)
               # print(tree_source + ' copied to ' + tree_destination)

def remove_files(source, destination, filelist):
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
    filelist : li
        list of strings of filenames

    Returns
    -------
    Str
        Log of files removed
    '''
    for file in os.listdir(source):
        if file not in filelist:
            if not os.path.exists(destination):
                os.makedirs(destination)
            shutil.move(source + file, destination + file)
            print (source + file + " moved to " + destination + file)
    return

def run_actions():
    #Create Logs
    print ('LOG FILE ')
    print ('DATE: ' + str(datetime.date.today()))
    print('')
    print('')
    print('FILES REMOVED: ')
    print('')
    remove_files(path, date_path, filelist)
    print('')
    print('')
    print('BACKUPS CREATED: ')
    print('')
    create_backups(path,backup_destination,ignore_folder = ignore_folder)
    print('')
    print('')
    print('BACKUPS REMOVED: ')
    print('')
    clean_backups(integrity_path + "backups/",10)

def run():
    while(1==1):
        time = datetime.now()
        print(time)
        runtimes = (8,10,12,14,16)
        if time.hour == 7:
            create_filelist(path)
        if time.hour in runtimes:
            run_actions()
        sleep (60*(60-datetime.now().minute))
 
#Run

run()



        
