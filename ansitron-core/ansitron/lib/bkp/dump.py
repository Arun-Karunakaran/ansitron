#! /usr/bin/python3

import json, os, yaml, sys, ruamel.yaml
from handlers import ymlhandlers
from utilities import apimethods
from contextlib import redirect_stdout
from urllib import parse as prs

#__all__ = ['_dump_ymlasjson','_dump_playbookasjson']

class dumpdata_asfile(ymlhandlers,apimethods):
    """
    This class is for dumping and storing objects safely
    """
        
    @classmethod    
    def dump_ymlasjson(cls,*data):
        """

        Description:
        ------------
        This converts specified yml files to json and stores it in ansible root project directory under json folder or any folder as desirable
        
        Usage:  
        ------
        dumpdata_asfile(os.environ["PLAYBOOK_ABSOLUTE_DIR"]+"/install-cygwin64.yml",os.environ["ANSIBLE_PROJ_ROOT_DIR"]+"/json/install-cygwin.yml")
        dumpdata_asfile("/etc/ansible/install-python.yml")
        dumpdata_asfile.dump_ymlasjson()
        
        Parameters:
        ----------
        Path : values : <any directory that contains yml files>

        Returns:
        -------
        None

        """
        cls.set_jsondir()
        os.chdir(cls.get_jsondir())
        cls.convert_ymltojson(data[0], cls.get_jsondir() + "/" + cls.append_filetypasjson(cls.extract_pathbasename(data[0])))
        cls.reset_toprojpath()

    @classmethod
    def dump_playbookasjson(cls,*data):
        """

        Description:
        -----------
        This function converts yml files in specified playbook directory into json into a seperate json folder under project root directory only.

        Usage:
        -----
        dumpdata_asfile(os.environ["PLAYBOOK_ABSOLUTE_DIR"])
        dumpdata_asfile(os.environ["ANSIBLE_PROJ_ROOT_DIR"])
        dumpdata_asfile.dump_playbookasjson()

        Parameters
        ---------
        Path : values : <directory path where collection of yml files located>
                        takes envs : $PLAYBOOK_ABSOLUTE_DIR or $ANSIBLE_PROJ_ROOT_DIR or path where collectiion of yml files located
                        Conditions: never takes relative paths as param
            
        Returns
        -------
        None

        """
        cls.set_jsondir()
        os.chdir(cls.get_jsondir())
        cls.convert_ymlstojsons(data[0], cls.get_jsondir())
        cls.reset_toprojpath()

    @classmethod
    def dump_envasjson(cls,*data):
        """
        
        Description: 
        ------------
        This function is used for dumping environment variables as json to json folder path
        
        Usage:
        ------
        dumpdata_asfile('env')
        dumpdata_asfile.dump_envasjson()

        Parameters
        ---------
        Path : values : filename
                        takes: single argument as param

        Returns
        -------
        None

        """
        cls.set_jsondir()
        os.chdir(cls.get_jsondir())
        with open(os.path.splitext(data[0])[0] + '.json', 'w') as f:
            with redirect_stdout(f):
                print(json.dumps(dict(os.environ)))
        cls.reset_toprojpath()

    @classmethod
    def dump_playbookasformatdyml(cls,*data):
        """

        Description:
        ------------
        This function is used for dumping yml as formatted yml in the playbook dir

        Usage:
        ------
        dumpdata_asfile(os.environ["PLAYBOOK_ABSOLUTE_DIR"])
        dumpdata_asfile.dump_playbookasformatdyml()

        Parameters
        ---------
        Path : values : filename
                        takes: single argument as param

        Returns
        -------
        None

        """
        cls.set_formatdymldir()
        os.chdir(cls.get_formatdymldir())
        cls.convert_ymlsasformatdymls(data[0], cls.get_formatdymldir())
        cls.reset_toprojpath()

class dumpdata_asdb:

    def dump_jsontopostgres(self):
        """

        Description:
        ------------
        This function dumps json to db for permanent storage.

        Usage:
        -----
        

        """

if __name__ == "__main__":
    import sys
    dumpdata_asfile.dump_playbookasformatdyml(sys.argv[1])
