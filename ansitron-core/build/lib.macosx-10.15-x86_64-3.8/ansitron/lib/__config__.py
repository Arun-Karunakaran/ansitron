#! /usr/bin/python3

import configparser
import os
config = configparser.ConfigParser()

__all__=['get_config','set_config','remove_config','list_config','print_config']

if os.path.exists(os.path.join('/tmp','ansitron.ini')):
    __configfile__ = os.path.join('/tmp','ansitron.ini')
else:
    __configfile__ = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config', 'ansitron.ini')

class get_config:

    def __init__(self, section, name=None):

        self.section = section
        self.name = name

    def getsectionkey(self):

        config.read(__configfile__)
        return config.get(self.section, self.name)

    def getsection(self):

        config.read(__configfile__)
        return config.items(self.section)

class set_config:

    def  __init__(self, section, name=None, value=None):
        
        self.section = section
        self.name = name
        self.value = value 

    def addsectionitems(self):
        
        config.read(__configfile__)
        config.add_section(self.section)
        config.set(self.section, self.name, self.value)
        with open(__configfile__, 'w') as configfile:
            config.write(configfile)
        configfile.close()
        print(config.read(__configfile__))


    def updatesectionitems(self):

        config.read(__configfile__)
        config.set(self.section, self.name, self.value)
        with open(__configfile__, 'w') as configfile:
            config.write(configfile)
        configfile.close()
        ###print(config.read(__configfile__))


class remove_config:

    def  __init__(self, section, name=None):

        self.section = section
        self.name = name if name is not None else None

    def deletesection(self):

        config.read(__configfile__)
        config.remove_section(self.section)
        with open(__configfile__, 'w') as configfile:
            config.write(configfile)
        configfile.close()
        #print(config.read(__configfile__))

    def deletesectionkey(self):

        config.read(__configfile__)
        config.remove_option(self.section, self.name)
        with open(__configfile__, 'w') as configfile:
            config.write(configfile)
        configfile.close()
        #print(config.read(__configfile__))


class list_config:

    def __init__(self,section):

        self.section = section

    def list_section(self):
        
        config.read(__configfile__)
        return list(config.items(self.section))

def print_config():

    config.read(__configfile__)
    for sect in config.sections():
        print("\n",sect)
        for k,v in config.items(sect):
            print(k +" : "+ v)

if __name__ == "__main__":
    #print_config()
    l = list_config('test1')
    l.list_section()
