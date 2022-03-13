#! /usr/bin/python3

import os

class _getdir():


    def get_projdir(self):
        """
        This function returns the ansible project root directory
        """
        projroot = os.getenv('ANSIBLE_PROJ_ROOT_DIR')
        return projroot

    def get_jsondir(self):
        """
        This function returns the json folder directory where all playbook json files are located
        """
        jsondirpath = os.path.join(self.get_projdir(), self.get_jsonfolder())
        return jsondirpath

    def get_ymlbkpdir(self):
        """
        This function returns the ymlbkp folder directory where all playbooks yml bkp files are located
        """
        ymlbkppath = os.path.join(self.get_projdir(), self.get_ymlbkpfolder())
        return ymlbkppath

    def get_formatdymldir(self):
        """
        This function returns the formatted yml folder directory where all playbooks formatted yml files are located
        """
        formatdymlpath = os.path.join(self.get_playbookabsdir(), self.get_formatdymlfolder())
        return formatdymlpath

    def get_playbookreldir(self):
        """
        This function returns the playbooks relative path directory where all playbook yml files are located.
        """
        pbookrelpath = os.path.relpath(self.get_playbookabsdir(), self.get_projdir())
        return pbookrelpath

    def get_playbookabsdir(self):
        """
        This function returns the playbook absolute path directory where all playbook yml files are located.
        """
        pbookabspath = os.getenv('PLAYBOOK_ABSOLUTE_DIR')
        return pbookabspath
        
    def get_jsonfolder(self):
        """
        Gets the json folder name
        """
        jsonfolder = os.getenv('JSON_FOLDER_NAME')
        return jsonfolder

    def get_ymlbkpfolder(self):
        """
        Gets the yml bkp folder name
        """
        ymlbkpfolder = os.getenv('YML_BKP_FOLDER_NAME')
        return ymlbkpfolder

    def get_formatdymlfolder(self):
        """
        Gets the formatted yml folder name
        """
        ymlformatdfldr = os.getenv('FORMATTED_YML_FOLDER_NAME')
        return ymlformatdfldr

class _setdir():


    def set_jsondir(self):
        """
        This function creates the json folder directory where all playbook json files are located
        """ 
        getdir = _getdir()
        jsonpath = os.path.join(getdir.get_projdir(), getdir.get_jsonfolder())
        if not os.path.exists(jsonpath):
            os.mkdir(jsonpath)

    def set_ymlbkpdir(self):
        """
        This function creates the yml bkp folder directory. Here all the manually converted json to yml files are stored as bkp or it  stores json retreived from database in yml converted format. Thus serves as a backup for all playbook yml files
        """
        getdir = _getdir()
        ymlbkppath = os.path.join(getdir.get_projdir(), getdir.get_ymlbkpfolder())
        if not os.path.exists(ymlbkppath):
            os.mkdir(ymlbkppath)

    def set_formatdymldir(self):
        """
        This function creates the formatted yml folder where all playbook yml files are formatted and stored.
        """
        getdir = _getdir()
        formatdymldir = getdir.get_formatdymldir()
        if not os.path.exists(formatdymldir):
            os.mkdir(formatdymldir)


class _reset:


    def reset_path(self):
        """
        This function resets path to the ansible projects root directory
        """
        getdir = _getdir()
        projroot = getdir.get_projdir()
        os.chdir(projroot)

if __name__ == "__main__":
    setdir = _setdir()
    setdir.set_ymlbkpdir()
