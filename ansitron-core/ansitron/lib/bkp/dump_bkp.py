#! /usr/bin/python3

import json, os, yaml, sys, ruamel.yaml 
import getdp
from contextlib import redirect_stdout

class dumpas:
    """
    This class is for dumping and storing objects safely
    """

    def __init__(self,flin,flout):
        self.flin = flin if flin is not None else []
        self.flout = flout if fileout is not None else []
    
    def dumpyml_asjson(self):
        """
        This converts specified yml files to json and stores it in ansible root project directory under json folder
        """
        yaml = ruamel.yaml.YAML(typ='safe')
        os.chdir(getdp.get_jsondir())
        with open(self.flin) as inp:
            data = yaml.load(inp)
        with open(self.flout, 'w') as out:
            json.dump(data, out, indent=2)
        getdp.resetpath()

    def dumpplaybooks_asjson():
        """
        This playbook finds and converts all yml files to json into a specified folder.
        """
        yaml = ruamel.yaml.YAML(typ='safe')
        projdir = getdp.get_projdir()
        for filename in os.listdir(projdir):
            if filename.endswith(".yml"):
                os.chdir(getdp.get_projdir())
                with open(filename) as inp:
                    data = yaml.load(inp)
                os.chdir(getdp.get_jsondir())
                with open(os.path.splitext(filename)[0] + '.json', 'w') as out:
                    json.dump(data, out, indent=2)
        getdp.resetpath()

    def dumpenv_asjson():
        """
        This function is used for dumping environment variables as json
        """
        os.chdir(getdp.get_jsondir())
        with open('env.json', 'w') as f:
            with redirect_stdout(f):
                print(json.dumps(dict(os.environ)))
        getdp.resetpath()

    def dumpjson_todb(self):
        """
        This function dumps json to db for permanent storage.
        """
