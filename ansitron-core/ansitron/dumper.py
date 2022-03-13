#! /usr/bin/python3

import json, os, yaml, sys, ruamel.yaml
from .lib.handlers import ymlhandlers
from .lib.utilities import apimethods
from contextlib import redirect_stdout
from urllib import parse as prs

__all__ = ['dumpdata_asfile','dumpdata_asdb']

class dumpdata_asfile:
    """
    This class is for dumping and storing objects safely
    """
    def __init__(self,datain=None,dataout=None):
        self.datain = datain
        self.dataout = dataout
        
    @staticmethod    
    def dump_ymlasjson(*data):
        """

        Description:
        ------------
        This converts specified yml files to json and stores it in ansible root project directory under json folder or any folder as desirable
        
        Usage:  
        ------
        dumpdata_asfile.dump_ymlasjson(os.environ["PLAYBOOK_ABSOLUTE_DIR"]+"/install-cygwin64.yml",os.environ["ANSIBLE_PROJ_ROOT_DIR"]+"/json/install-cygwin.yml")
        dumpdata_asfile.dump_ymlasjson("/etc/ansible/install-python.yml")
        
        Parameters:
        ----------
        Path : values : <any directory that contains yml files>

        Returns:
        -------
        None

        """
        apimethods.set_jsondir()
        os.chdir(apimethods.get_jsondir())
        ymlhandlers.convert_ymltojson(data[0], apimethods.get_jsondir() + "/" + ymlhandlers.append_filetypasjson(ymlhandlers.extract_pathbasename(data[0])))
        apimethods.reset_toprojpath()

    @staticmethod
    def dump_playbookasjson(*data):
        """

        Description:
        -----------
        This function converts yml files in specified playbook directory into json into a seperate json folder under project root directory only.

        Usage:
        -----
        dumpdata_asfile.dump_playbookasjson(os.environ["PLAYBOOK_ABSOLUTE_DIR"])
        dumpdata_asfile.dump_playbookasjson(os.environ["ANSIBLE_PROJ_ROOT_DIR"])

        Parameters
        ---------
        Path : values : <directory path where collection of yml files located>
                        takes envs : $PLAYBOOK_ABSOLUTE_DIR or $ANSIBLE_PROJ_ROOT_DIR or path where collectiion of yml files located
                        Conditions: never takes relative paths as param
            
        Returns
        -------
        None

        """
        apimethods.set_jsondir()
        os.chdir(apimethods.get_jsondir())
        ymlhandlers.convert_ymlstojsons(data[0], apimethods.get_jsondir())
        apimethods.reset_toprojpath()

    @staticmethod
    def dump_envasjson(*data):
        """
        
        Description: 
        ------------
        This function is used for dumping environment variables as json to json folder path
        
        Usage:
        ------
        dumpdata_asfile.dump_envasjson('env')

        Parameters
        ----------
        Path : values : filename
                        takes: single argument as param

        Returns
        -------
        None

        """
        apimethods.set_jsondir()
        os.chdir(apimethods.get_jsondir())
        with open(os.path.splitext(data[0])[0] + '.json', 'w') as f:
            with redirect_stdout(f):
                print(json.dumps(dict(os.environ)))
        apimethods.reset_toprojpath()

    @staticmethod
    def dump_playbookasformatdyml(*data):
        """

        Description:
        ------------
        This function is used for dumping yml as formatted yml in the playbook dir

        Usage:
        ------
        dumpdata_asfile.dump_playbookasformatdyml(os.environ["PLAYBOOK_ABSOLUTE_DIR"])

        Parameters
        ----------
        Path : values : filename
                        takes: single argument as param

        Returns
        -------
        None

        """
        apimethods.set_formatdymldir()
        os.chdir(apimethods.get_formatdymldir())
        ymlhandlers.convert_ymlsasformatdymls(data[0], apimethods.get_formatdymldir())
        apimethods.reset_toprojpath()


    def dump_filetoremote(self):
        """

        """

class dumpdata_asdb:

    def dump_jsontopostgres(self):
        """

        Description:
        ------------
        This function dumps json to db for permanent storage.

        Usage:
        -----
        dumpdata_asdb.dump_jsontopostgres

        """

    def dump_filetoremotedb(self):
        """

        """

if __name__ == "__main__":
    import os
    dumpdata_asfile.dump_ymlasjson('/var/lib/awx/tasks/test.yml')
