#! /usr/bin/python3

#from ansitron.bin import ansitron_actions, ansitron_builder
import sys, os, hashlib, ctypes, configparser, fnmatch
from ansitron.lib import __config__, handlers
from ansitron.bin.ansitron_builder import _prompt_dotatronenv, _prompt_config, _builddefaults_dotatronenv, _builddefaults_config, _buildactions
#from ansitron.bin.ansitronliccheck import _licensecheck, _md5sum

#__all__=['build_ansitron']

os.environ['MY_PACKAGE_ROOT'] = os.path.dirname(os.path.abspath(__file__))
#licfilenm = os.path.join(os.environ['MY_PACKAGE_ROOT'], 'LICENSE.md')


def build_ansitron():

    _buildactions()

def main():
    
#    __license__ = (_licensecheck(lambda: _md5sum(licfilenm, 65536)))
#    if __license__ != 'License check passed':   
#        print('License check failed. Add a valid license')
#        sys.exit()
#    else:
    build_ansitron()


if __name__ == "__main__":
#    get_version()
    main() 
    #print(__license__)
    #print(md5sum(licfilenm, 65536))
