#! /usr/bin/python3

import os
from .__config__ import *

__all__ = ['apimethods']

class _getdir:

        
    @staticmethod
    def get_projdir():
        """
        This function returns the ansible project root directory
        """
        cg = get_config('environvars:','ANSIBLE_PROJ_ROOT_DIR')
        projroot = cg.getsectionkey()
        return projroot
    
    @staticmethod
    def get_playbookabsdir():
        """
        This function returns the playbook absolute path directory where all playbook yml files are located.
        """
        cg = get_config('environvars:','PLAYBOOK_ABSOLUTE_DIR')
        pbookabspath = cg.getsectionkey()
        return pbookabspath

    @staticmethod
    def get_jsonfolder():
        """
        Gets the json folder name
        """
        cg = get_config('environvars:','JSON_FOLDER_NAME')
        jsonfolder = cg.getsectionkey()
        return jsonfolder

    @staticmethod
    def get_ymlbkpfolder():
        """
        Gets the yml bkp folder name
        """
        cg = get_config('environvars:','YML_BKP_FOLDER_NAME')
        ymlbkpfolder = cg.getsectionkey()
        return ymlbkpfolder

    @staticmethod
    def get_formatdymlfolder():
        """
        Gets the formatted yml folder name
        """
        cg = get_config('environvars:','FORMATTED_YML_FOLDER_NAME')
        ymlformatdfldr = cg.getsectionkey()
        return ymlformatdfldr

    @classmethod
    def get_jsondir(cls):
        """
        This function returns the json folder directory where all playbook json files are located
        """
        jsondirpath = os.path.join(cls.get_projdir(), cls.get_jsonfolder())
        return jsondirpath

    @classmethod
    def get_ymlbkpdir(cls):
        """
        This function returns the ymlbkp folder directory where all playbooks yml bkp files are located
        """
        ymlbkppath = os.path.join(cls.get_projdir(), cls.get_ymlbkpfolder())
        return ymlbkppath

    @classmethod
    def get_formatdymldir(cls):
        """
        This function returns the formatted yml folder directory where all playbooks formatted yml files are located
        """
        formatdymlpath = os.path.join(cls.get_playbookabsdir(), cls.get_formatdymlfolder())
        return formatdymlpath

    @classmethod
    def get_playbookreldir(cls):
        """
        This function returns the playbooks relative path directory where all playbook yml files are located.
        """
        pbookrelpath = os.path.relpath(cls.get_playbookabsdir(), cls.get_projdir())
        return pbookrelpath


class _setdir(_getdir):


    @classmethod
    def set_jsondir(cls):
        """
        This function creates the json folder directory where all playbook json files are located
        """ 
        #getdir = _getdir()
        jsonpath = os.path.join(cls.get_projdir(), cls.get_jsonfolder())
        if not os.path.exists(jsonpath):
            os.mkdir(jsonpath)

    @classmethod
    def set_ymlbkpdir(cls):
        """
        This function creates the yml bkp folder directory. Here all the manually converted json to yml files are stored as bkp or it  stores json retreived from database in yml converted format. Thus serves as a backup for all playbook yml files
        """
        #getdir = _getdir()
        ymlbkppath = os.path.join(cls.get_projdir(), cls.get_ymlbkpfolder())
        if not os.path.exists(ymlbkppath):
            os.mkdir(ymlbkppath)
    
    @classmethod
    def set_formatdymldir(cls):
        """
        This function creates the formatted yml folder where all playbook yml files are formatted and stored.
        """
        #getdir = _getdir()
        formatdymldir = cls.get_formatdymldir()
        if not os.path.exists(formatdymldir):
            os.mkdir(formatdymldir)


class _reset(_getdir):


    @classmethod
    def reset_toprojpath(cls):
        """
        This function resets path to the ansible projects root directory
        """
        #getdir = _getdir()
        projroot = cls.get_projdir()
        os.chdir(projroot)


class apimethods(_reset,_setdir):

    @classmethod
    def apimethd(cls):
        print("found")

if __name__ == "__main__":
    apimethods.apimethd()
