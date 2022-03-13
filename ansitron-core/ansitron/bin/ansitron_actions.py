#! /usr/bin/python3

from ansitron.dumper import dumpdata_asfile as daf, dumpdata_asdb as dad
from ansitron.lib.utilities import apimethods
import os, sys

__all__ = ['process_playbook','store_playbook','retreive_playbook']

def process_playbook():
    """

    usage: ansitron-pbook-process [-h] {--formatymls | --backupymls | --ymlstojson | --allactions} ...

    argument options:
        {formatymls,backupymls,ymlstojson,allactions,help}
        
        Arguments:          Description:
        ----------          ------------
        formatymls          This formats the playbook ymls and dumps the formatted files into a folder
        backupymls          It just backsup the playbook ymls files into a seperate folder
        ymlstojson          It converts the ymls of playbook dir to jsons and dumps in a folder
        allactions          This does the combined actions of the all the arguments
        help                Show this help

    optional arguments:
        -h, -help            show this help message ans exit

    returns:
        success message

    """

    try:
        if sys.argv[1] == '--formatymls':
            daf.dump_playbookasformatdyml(os.environ["PLAYBOOK_ABSOLUTE_DIR"])
            print('Formatted ymls is placed in dir: ', '\n\t' + os.environ["PLAYBOOK_ABSOLUTE_DIR"] + '/' + apimethods.get_formatdymlfolder())
        elif sys.argv[1] == '--ymlstojson':
            daf.dump_playbookasjson(os.environ["PLAYBOOK_ABSOLUTE_DIR"] + '/' + apimethods.get_formatdymlfolder())
            print('ymls converted to json is placed in dir: ', os.environ["ANSIBLE_PROJ_ROOT_DIR"] + '/' + apimethods.get_jsonfolder())
    #elif argv[0] == 'backup':
        #daf.dump_playbookasbackup
        elif sys.argv[1] == '--allactions':
            daf.dump_playbookasformatdyml(os.environ["PLAYBOOK_ABSOLUTE_DIR"])
            daf.dump_playbookasjson(os.environ["PLAYBOOK_ABSOLUTE_DIR"] + '/' + apimethods.get_formatdymlfolder())
            print('List of formatted ymls: ', os.listdir(os.environ["PLAYBOOK_ABSOLUTE_DIR"] + '/' + apimethods.get_formatdymlfolder()))
            print('List of ymls converted as jsons: ', os.listdir(os.environ["ANSIBLE_PROJ_ROOT_DIR"] + '/' + apimethods.get_jsonfolder()))
        #daf.dump_playbookasbackup
        elif sys.argv[1] == '-help' or sys.argv[1] == '-h' or sys.argv[1] == '/h' or sys.argv[1] == '/help':
            print(process_playbook.__doc__)
    except IndexError:
        print(process_playbook.__doc__)


def store_playbook(*argv):
    """

        Description:
        ------------
        This script stores playbook data as per user specific choice and need.

        Usage:
        ------
        store_playbook(<param>)

        Parameters:
        ----------
        string : values : asjson | intopostgres | allactions

        Returns:
        -------
        None

    """

    if argv[0] == 'asjson':
        daf.dump_playbookasjson(os.environ["PLAYBOOK_ABSOLUTE_DIR"] + '/' + apimethods.get_formatdymlfolder())
    elif argv[0] == 'intopostgres':
        dad.dump_jsontopostgres(os.environ["ANSIBLE_ROOT_PROJ_DIR"] + '/' + apimethods.get_jsonfolder())
    elif argv[0] == 'allactions':
        daf.dump_playbookasjson(os.environ["PLAYBOOK_ABSOLUTE_DIR"] + '/' + apimethods.get_formatdymlfolder())
        dad.dump_jsontopostgres(os.environ["ANSIBLE_ROOT_PROJ_DIR"] + '/' + apimethods.get_jsonfolder())

def retreive_playbook(*argv):
    """

        Description:
        ------------
        This script retreive yml data as per user specific choice and need. This is used when you have lost all your playbooks and need to retreive it from permanently stored locations.

        Usage:
        ------
        retreive_playbook(<param>)

        Parameters:
        ----------
        string : values : frompostgresasymls | frompostgresasjson | allactions

        Returns:
        -------
        None
    """


#if __name__ == "__main__":
    
