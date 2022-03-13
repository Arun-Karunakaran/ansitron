#! /usr/bin/python3

from ansitron.lib.__config__ import set_config
from ansitron.lib.handlers import filehandlers
from ansitron.loader import dotatronenv
import os, sys, configparser

#__all__ = ['load_config']
os.environ['MY_PACKAGE_ROOT'] = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class build:

    def test():
        print("This works")

def buildactions():
    """

    usage: ansitron-builder [-h] {--dotatronenv|--config|--postgresdb|--mongodb} ...

    argument options:
        {dotatronenv,config,help}

        Arguments:          Description:
        ----------          ------------
        dotatronenv         builds basic/required .atronenv file for ansitron
        config              builds basic/required config as necessary for ansitron
        postgres            builds basic/required postgresdb setup  as necessary for ansitron
        mongodb             builds basic/required mongodb setup  as necessary for ansitron
        help                Show this help

    optional arguments:
        -h, -help            show this help message ans exit

    returns:
        success message

    """
    try:
        if sys.argv[1] == '--dotatronenv':
            _prompt_dotatronenv()
            dotatronenvpath = os.path.join(os.getenv('HOME'),'.atronenv')
            if os.path.exists(dotatronenvpath):
                if dotatronenv.load_dotatronenv(dotatronenv.find_dotatronenv()):
                    if dotatronenv.get_dotatronenv('ANSIBLE_PROJ_ROOT_DIR') != False and dotatronenv.get_dotatronenv('PLAYBOOK_ABSOLUTE_DIR') != False and dotatronenv.get_dotatronenv('JSON_FOLDER_NAME') != False and dotatronenv.get_dotatronenv('YML_BKP_FOLDER_NAME') != False and dotatronenv.get_dotatronenv('FORMATTED_YML_FOLDER_NAME') != False:
                        print ("Msg: A matching dotatronenv with defaults already found in path: %s\n " % dotatronenvpath)
                        raise SystemExit(0)
                    else:
                        print("Msg: Required default item keys for dotatronenv is not found in file: %s " % dotatronenvpath)
                        _prompt_dotatronenv()
                        _builddefaults_dotatronenv()
                else:
                    raise Exception("Msg: unable to load dotatronenv")
                    sys.exit()
            else:
                _builddefaults_dotatronenv()
        elif sys.argv[1] == '--config':
            _prompt_config()
            _builddefaults_config()
        elif sys.argv[1] == '-help' or  sys.argv[1] == '-h' or sys.argv[1] == '/h' or sys.argv[1] == '/help':
            print(buildactions.__doc__)
    except IndexError:
        print(buildactions.__doc__)



def _buildactions(path=os.getenv('HOME')):

    _prompt_dotatronenv()
    dotatronenvpath = os.path.join(path,'.atronenv')
    if os.path.exists(dotatronenvpath):
        if dotatronenv.load_dotatronenv(dotatronenv.find_dotatronenv()):
            if dotatronenv.get_dotatronenv('ANSIBLE_PROJ_ROOT_DIR') == 'None' and dotatronenv.get_dotatronenv('PLAYBOOK_ABSOLUTE_DIR') == 'None' and dotatronenv.get_dotatronenv('JSON_FOLDER_NAME') != False and dotatronenv.get_dotatronenv('YML_BKP_FOLDER_NAME') != False and dotatronenv.get_dotatronenv('FORMATTED_YML_FOLDER_NAME') != False:
                print ("Msg: A matching dotatronenv with defaults already found in path: %s\n " % dotatronenvpath)
                _prompt_config()
                _builddefaults_config()
            else:
                print("Msg: Required default item keys for dotatronenv is not found in file: %s " % dotatronenvpath)
                _prompt_dotatronenv()
                _builddefaults_dotatronenv()
                _prompt_config()
                _builddefaults_config()
        else:
            raise Exception("Msg: unable to load dotatronenv")
            sys.exit()
    else:
        _builddefaults_dotatronenv()
        _prompt_config()
        _builddefaults_config()


def _prompt_dotatronenv(path=os.getenv('HOME')):

    dotatronenvpath = os.path.join(path,'.atronenv')
    value = input("\nMsg: This will Initiate/Alter to default .atronenv in path %s, \nDo you wish to proceed y/N: (default y)" % dotatronenvpath.rstrip('.atronenv')) or 'Y'
    if value is 'Y' or value is 'y':
        pass
    else:
        raise SystemExit(0)


def _prompt_config(path=os.path.join(os.environ.get('MY_PACKAGE_ROOT'),'config'),obj='ansitron.ini'):

    configfilepath = os.path.join(path,obj)
    value = input("\nMsg: This will Initiate/Alter to default config ansitron.ini in path %s with .atronenv as base, \nDo you wish to proceed y/N: (default y)" % configfilepath.rstrip('ansitron.ini')) or 'Y'
    if value is 'Y' or value is 'y':
        pass
    else:
        raise SystemExit(0)


def _builddefaults_dotatronenv(path=os.getenv('HOME')):

    dotatronenvpath = os.path.join(path,'.atronenv')
    file1 = open(dotatronenvpath, "w")
    file1.write("# environvars\n")
    file1.close()
    if dotatronenv.load_dotatronenv(dotatronenv.find_dotatronenv(path)):
        file1 = open(dotatronenvpath, "a+")
        file1.write("ANSIBLE_PROJ_ROOT_DIR = None\n")
        file1.write("PLAYBOOK_ABSOLUTE_DIR = None\n")
        file1.write("JSON_FOLDER_NAME = json\n")
        file1.write("YML_BKP_FOLDER_NAME = ymlbkp\n")
        file1.write("FORMATTED_YML_FOLDER_NAME = formattedyml\n")
        file1.close()
        print("Msg: successfully loaded dotatronenv with defaults")
    else:
        raise Exception("Msg: unable to load dotatronenv")
        sys.exit()


def _builddefaults_config(atronpath=os.getenv('HOME'),configpath=os.path.join(os.environ.get('MY_PACKAGE_ROOT'),'config'),obj='ansitron.ini'):

    configfilepath = os.path.join(configpath,obj)
    config = configparser.ConfigParser()
    config.clear()
    file1 = open(configfilepath, "w")
    file1.write("[environvars:]\n")
    file1.close()
    if dotatronenv.load_dotatronenv(dotatronenv.find_dotatronenv(atronpath)):
        c1 = set_config('environvars:','ANSIBLE_PROJ_ROOT_DIR',"{0}".format(dotatronenv.get_dotatronenv('ANSIBLE_PROJ_ROOT_DIR',path=atronpath)))
        c2 = set_config('environvars:','PLAYBOOK_ABSOLUTE_DIR',"{0}".format(dotatronenv.get_dotatronenv('PLAYBOOK_ABSOLUTE_DIR',path=atronpath)))
        c3 = set_config('environvars:','JSON_FOLDER_NAME',"{0}".format(dotatronenv.get_dotatronenv('JSON_FOLDER_NAME',path=atronpath)))
        c4 = set_config('environvars:','YML_BKP_FOLDER_NAME',"{0}".format(dotatronenv.get_dotatronenv('YML_BKP_FOLDER_NAME',path=atronpath)))
        c5 = set_config('environvars:','FORMATTED_YML_FOLDER_NAME',"{0}".format(dotatronenv.get_dotatronenv('FORMATTED_YML_FOLDER_NAME',path=atronpath)))
        c1.updatesectionitems()
        c2.updatesectionitems()
        c3.updatesectionitems()
        c4.updatesectionitems()
        c5.updatesectionitems()
        del c1, c2, c3, c4, c5
        print("Msg: successfully loaded config with defaults")
    else:
        raise Exception("Msg: unable to load dotatronenv")
        sys.exit()


#def _buildobjects(_builddefaults_dotatronenv,_builddefaults_config):

#    pass

#def main():
    
#    _buildobjects()    

#if __name__ == "__main__":
#    _prompt_dotatronenv(path='/tmp')
