#! /usr/bin/python3

from ansitron.lib.utilities import *
from ansitron.lib.handlers import *
#from ansitron.bin.ansitron_builder import *
from ansitron.dumper import *
from ansitron.loader import *
#from datetime import date
import sys, os

__all__ = ['dumpdata_asfile','dumpdata_asdb','apimethods','ymlhandlers','filehandlers','dotatronenv','dotatron']

os.environ['MY_PACKAGE_ROOT'] = os.path.dirname(os.path.abspath(__file__))
configvarstore= os.path.join(os.environ['MY_PACKAGE_ROOT'], 'config/varstore.dat')
f = filehandlers.parsekeyvaluepairs(configvarstore)

__name__ = f['name'].rstrip("\n")
__author__ = f['author'].rstrip("\n")
__version__ =  format(float(f['version']),".2f").rstrip("\n")
__copyright__ = f['copyright'].rstrip("\n")
__date__ = f['date'].rstrip("\n")
__email__ = f['email'].rstrip("\n")
__status__ = f['status'].rstrip("\n")
__releaseinfo__ =f['releaseinfo'].rstrip("\n")

def ansitrone():

    """

    usage: ansitron [-h] {--version} ...

    argument options:
        {version,help}

        Arguments:          Description:
        ----------          ------------
        version             returns version of ansitron
        help                Show this help

    optional arguments:
        -h, -help            show this help message ans exit

    returns:
        version no

    """
    try:
        if sys.argv[1] == "--version":
            print(__name__ +" " +__version__)
        elif sys.argv[1] == '-help' or  sys.argv[1] == '-h' or sys.argv[1] == '/h' or sys.argv[1] == '/help':
            print(ansitrone.__doc__)
    except IndexError:
        print(ansitrone.__doc__)
