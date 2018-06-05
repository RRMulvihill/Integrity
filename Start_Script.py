'''
START_SCRIPT
by Riley Mulvihill

Start_Script should be run by a sheduled task through Start.cmd
which exports the output as filelist.txt

Start_Script should be run in the morning on a daily basis BEFORE End_Script.py

Start_Script creates a list of all the files in the software root folder.
Default root path is C:/TestGenius
'''

import os
from Imports import *

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

create_filelist(path)
