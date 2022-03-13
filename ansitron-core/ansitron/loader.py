#! /usr/bin/python3

from .lib.handlers import filehandlers
from pathlib import Path
import os

class dotatronenv:

    path=os.getenv('HOME')
    objname='.atronenv'

    def __init__(self, path:str=None, objname:str=None):

        self.path = path
        self.objname = objname

    @staticmethod
    def find_dotatronenv(path=os.getenv('HOME'), objname='.atronenv'):

        try:
            if filehandlers.find_objectpath(objname,path) != False:
                return filehandlers.find_objectpath(objname,path)
            else:
                return False
        except KeyError:
            return False


    @staticmethod
    def load_dotatronenv(func):
        
        try:
            if func != False:
                return True
            else:
                return False
        except KeyError:
            return False
    
    @classmethod
    def get_dotatronenv(cls, keyname:str, path=os.getenv('HOME')):

        try:
            if cls.load_dotatronenv(cls.find_dotatronenv(path, cls.objname)):
                #path=cls.find_dotatronenv(path, cls.objname).rstrip(".atronenv")
                atronenv = filehandlers.parsekeyvaluepairs(path+"/"+cls.objname)
                return atronenv[keyname].rstrip("\n").lstrip(" ")
            else:
                return False
        except KeyError:
            return False

    @classmethod
    def alter_dotatronenv(cls, keyname:str, value, path=os.getenv('HOME')):

        try:
            if cls.load_dotatronenv(cls.find_dotatronenv(path, cls.objname)):
                #path=cls.find_dotatronenv().rstrip(".atronenv")
                if cls.get_dotatronenv(keyname, path) != False:
                    gotval = cls.get_dotatronenv(keyname, path)
                    srcval = keyname+" = "+gotval
                    rplcval = keyname+" = "+value
                    pass
                else:
                    return False
                if filehandlers.count_filedata(path+"/"+cls.objname, srcval) == 1:
                    pass
                else:
                    raise Exception("More than one data found. cannot alter!!!")
                check = filehandlers.replace_filedata(path+"/"+cls.objname, srcval, rplcval)
                if isinstance(check, int):    
                    return True
                else:
                    return False
            else:
                return False
        except KeyError:
            return False


class dotatron:

    path=os.getenv('HOME')
    objname='.atron'

    def __init__(self, path:str=None, objname:str=None):

        self.path = path
        self.objname = objname

    @staticmethod
    def find_dotatron(objname='.atron', path=os.getenv('HOME')):

        if filehandlers.find_objectpath(objname,path) != False:
            return filehandlers.find_objectpath(objname,path)
        else:
            return filehandlers.find_objectpath(objname,path='/')


    @classmethod
    def load_dotatron(cls,path:str=os.getenv('HOME'), objname='.atron'):

        if os.path.exists(path+"/"+objname):
            return True
        elif cls.find_dotatron() != False:
            return True
        else:
            return False

    @classmethod
    def get_dotatron(cls, keyname:str):

        try:
            if cls.load_dotatron():
                path=cls.find_dotatron().rstrip(".atron")
                atron = filehandlers.parsekeyvaluepairs(path+"/"+cls.objname)
                return atron[keyname].rstrip("\n")
            else:
                return False
        except KeyError:
            return False
  


if __name__ == '__main__':
    print(dotatronenv.load_dotatronenv(dotatronenv.find_dotatronenv(path='/tmp')))
