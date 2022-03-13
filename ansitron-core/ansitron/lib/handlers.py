#! /usr/bin/python3

import mmap, urllib, ruamel.yaml, json, sys, os, fnmatch, hashlib

__all__=['filehandlers','ymlhandlers']

class filehandlers:

    @staticmethod
    def replace_filedata(*fileparam):
        """
    
            Description:
            ------------
            This function is used for replacing file data in a file
    
            Usage:
            ------
            filehandlers.replace_filedata('filename','search string','replace with string')
    
            Parameters
            ---------
            param1 : value : filename
            param2 : value : search for string or data
                             type : string
            param3 : value : replace with string or data
                             type : string
            Returns
            -------
            write data code value eg: 4117
    
        """
    
        if not fileparam:
            raise exception("No parameter passed: minimum 3 args required")
        with open(fileparam[0], 'rb', 0) as f, \
             mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as s:
            if s.find(fileparam[1].encode()) != -1:
                fin = open(fileparam[0], "rt")
                data = fin.read()
                data = data.replace(fileparam[1], fileparam[2])
                fin.close()
                fin = open(fileparam[0], "wt")
                check = fin.write(data)
                return check
                fin.close()
                #if type(check) == int:
                    #return True
                #fin.close()
            else:
                print('No match found')

    @staticmethod
    def search_filedata(*data):
        """
    
            Description:
            ------------
            This function is used for searching file data in a file
    
            Usage:
            ------
            filehandlers.search_filedata('filename','search for string')
    
            Parameters
            ---------
            param1 : value : filename
            param2 : value : search for string or data
                             type : string
    
            Returns
            -------
            bool
    
        """
    
        if not data:
            raise exception("No parameter passed: minimum 2 args required")
        with open(data[0], 'rb', 0) as f, \
             mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as s:
            if s.find(data[1].encode()) != -1:
                return True
            else:
                return False

    @staticmethod
    def count_filedata(*data):
        """

            Description:
            ------------
            This function is used for counting file data in a file

            Usage:
            ------
            filehandlers.count_filedata('filename','search string')

            Parameters
            ---------
            param1 : value : filename
            param2 : value : search for string or data
                      type : string

            Returns
            -------
            int : total count of search data

        """

        if len(data) != 2:
            raise exception("No of parameter passed: 2 args required")
        fin = open(data[0], 'r').read()
        cnt = fin.count(data[1])
        return cnt

    @staticmethod
    def findpattern(folderpattern,filepattern,path):
        """

            Description:
            ------------
            This function is used for retreiving the file path based on directory name and files inside the directory

            Usage:
            ------
            filehandlers.findpattern('foldername pattern','filename pattern, __file__)

            Parameters
            ---------
            param1 : value : folder pattern --> str
            param2 : value : file pattern --> str eg: *.yml
            param3 : value : current file path

            Returns
            -------
            path

        """
        try:
            result = []
            for root, dirs, files in os.walk(path):
                for name in dirs:
                        #print(name)
                    if fnmatch.fnmatch(name, folderpattern):
                        result.append(os.path.join(root,name))
            for path, dirs, files in os.walk(result[0]):
                if len(files) > 0:
                    for name in files:
                        if fnmatch.fnmatch(name, filepattern):
                            filecount = len(files)
                else:
                    print('File not found in %s' % folderpattern)
                    sys.exit()
            if filecount > 0:
                return result[0]
        except NameError:
            filecount = 0

    @staticmethod
    def find_objectpath(objname, path):
        """

            Description:
            ------------
            This function is used for finding any file or object in the file system. For locating the path

            Usage:
            ------
            filehandlers.findobjectpath(objname='.env')

            Parameters
            ---------
            param1 : value : object or file name --> str

            Returns
            -------
            bool
            str

        """

        try:
            list_of_files = {}
            for (dirpath, dirnames, filenames) in os.walk(path):
                for filename in filenames:
                    if filename.endswith(objname):
                        list_of_files[filename] = os.sep.join([dirpath, filename])
            return list_of_files[objname]
        except KeyError:
            return False


    @staticmethod
    def parsekeyvaluepairs(*data):
        """

            Description:
            ------------
            This function is used for parsing the key value pair data in a file

            Usage:
            ------
            filehandlers.parsekeyvaluepairs('filepathname')

            Parameters
            ---------
            param1 : value : filename

            Returns
            -------
            Key Value pairs
            bool

        """
       
        try:
            myvar = {}
            if len(data) != 1:
                raise exception("No of parameter passed: 1 arg required.")
            with open(data[0]) as f:
                for line in f:
                    key, value = line.partition("=")[::2]
                    myvar[key.strip()] = str(value)
                return myvar
        except FileNotFoundError:
            return False

    @staticmethod
    def _md5sum(filenm, blocksize=None):

        try:
            hash = hashlib.md5()
            with open(filenm, "rb") as f:
                for block in iter(lambda: f.read(blocksize), b""):
                    hash.update(block)
            return hash.hexdigest()
        except FileNotFoundError:
            print('File Not Found')
            sys.exit()

    @staticmethod
    def _md5sumcompare(filenm1, filenm2, blocksize=None):

        try:
            hash = hashlib.md5()
            hash2 = hashlib.md5()
            f1 = open(filenm1, "rb")
            for block in iter(lambda: f1.read(blocksize), b""):
                hash.update(block)
            f2 = open(filenm2, "rb")
            for block in iter(lambda: f2.read(blocksize), b""):
                hash2.update(block)
            #print(hash.hexdigest())
            #print(hash2.hexdigest())
            if int.from_bytes(bytes(hash.hexdigest()[:16], encoding='utf-8'), "big") == int.from_bytes(bytes(hash2.hexdigest()[:16], encoding='utf-8'), "big"):
                return True
            else:
                return False
        except FileNotFoundError:
            print('File Not Found')
            sys.exit()

class ymlhandlers:

    @staticmethod
    def format_yml():
        """
    
            Description:
            ------------
            This function is used for formating the yml files
    
            Usage:
            ------
            ymlhandlers.format_yml()
    
            Parameters
            ---------
            params : None
    
            Returns
            -------
            obj: formatted yml object using ruamel.yaml
    
        """
    
        yaml = ruamel.yaml.YAML()
        yaml.default_style=None
        yaml.default_flow_style=False
        yaml.indent=2
        yaml.preserve_quotes=True
        yaml.block_seq_indent=0
        yaml.explicit_start=True
        #yaml.compact_seq_map=False
        #yaml.compact(seq_map=False)
        yaml.sequence_dash_offset=0
        yaml.line_break=1
        yaml.encoding='utf-8'
        #yaml.version=='%YAML 1.2'
        return yaml

    @classmethod
    def convert_jsontoyml(cls,*argv):
        """
    
            Description:
            ------------
            This function is used for converting json to yml
    
            Usage:
            ------
            ymlhandlers.convert_jsontoyml('/etc/ansible/json/install-python.json','/etc/ansible/install-python.yml')
    
            Parameters
            ----------
            param1 : value : json filename with path
                     type  : string
            param2 : value : yml filename with path
                     type  : string
    
            Returns
            -------
            None
    
        """
    
        with open(argv[0]) as inp:
            data = json.load(inp)
        with open(argv[1], 'w') as out:
            yaml = cls.format_yml()
            yaml.dump(data, out)
    
    @classmethod
    def convert_ymltojson(cls,*argv):
        """
    
            Description:
            ------------
            This function is used for converting yml to json
    
            Usage:
            ------
            ymlhandlers.convert_ymltojson('/etc/ansible/install-python.yml','/etc/ansible/install-python.json')
    
            Parameters
            ----------
            param1 : value : yml filename with path
                     type  : string
            param2 : value : json filename with path
                     type  : string
    
            Returns
            -------
            None
    
        """
    
        with open(argv[0]) as inp:
            yaml = cls.format_yml()
            data = yaml.load(inp)
        with open(argv[1], 'w') as out:
            json.dump(data, out, indent=2)

    @classmethod
    def convert_ymlstojsons(cls,*argv):
        """

            Description:
            ------------
            This function is used for converting yml to json

            Usage:
            ------
            ymlhandlers.convert_ymlstojsons('/etc/ansible','/etc/ansible/json')

            Parameters
            ----------
            param1 : value : path of the yml file directory
                     type  : string
            param2 : value : path where the converted json files needs to reside
                     type  : string

            Returns
            -------
            None

        """
  
        for filename in os.listdir(argv[0]):
            if filename.endswith(".yml"):
                os.chdir(argv[0])
                with open(filename) as inp:
                    yaml = cls.format_yml()
                    data = yaml.load(inp)
                    os.chdir(argv[1])
                with open(argv[1] + "/" + os.path.splitext(filename)[0] + '.json', 'w') as out:
                    json.dump(data, out, indent=2)

    @classmethod
    def convert_ymlasformatdyml(cls,*argv):
        """
    
            Description:
            ------------
            This function is used for converting yml to a formatted yml 
    
            Usage:
            ------
            ymlhandlers.convert_ymlasformatdyml('/etc/ansible/install-python.yml','/etc/ansible/formatd/install-python.yml')
    
            Parameters
            ----------
            param1 : value : yml filename with path
                     type  : string
            parm2 : value : yml filename with path
                     type  : string
    
            Returns
            -------
            None
    
        """
    
        with open(argv[0]) as inp:
            yaml = format_yml()
            data = yaml.load(inp)
        with open(argv[1], 'w') as out:
            yaml.dump(data, out)

    @classmethod
    def convert_ymlsasformatdymls(cls,*argv):
        """

            Description:
            ------------
            This function is used for converting yml to a formatted yml

            Usage:
            ------
            ymlhandlers.convert_ymlasformatdyml('/etc/ansible','/etc/ansible/formatd')

            Parameters
            ----------
            param1 : value : yml filename with path
                     type  : string
            param2 : value : yml filename with path
                     type  : string

            Returns
            -------
            None

        """

        for filename in os.listdir(argv[0]):
            if filename.endswith(".yml"):
                os.chdir(argv[0])
                with open(filename) as inp:
                    yaml = cls.format_yml()
                    data = yaml.load(inp)
                    os.chdir(argv[1])
                with open(argv[1] + "/" + os.path.splitext(filename)[0] + '.yml', 'w') as out:
                    yaml.dump(data, out)

    @staticmethod
    def extract_pathbasename(*data):
        """
    
            Description:
            -----------
        """
    
        return os.path.basename(data[0])

    @staticmethod
    def append_filetypasjson(*data):
        """
    
            Description:
            ------------
        """
    
        return os.path.splitext(data[0])[0] + '.json'


if __name__ == '__main__':
    import os
    print(filehandlers.find_objectpath(objname='.atronenv'))
