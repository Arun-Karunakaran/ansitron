#! /usr/bin/python3

import mmap, urllib, ruamel.yaml, json, sys, os

class filehandlers:

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
                print(check)
                fin.close()
            else:
                print('No match found')


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
                print('true')
            else:
                print('false')

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
    print('count is: ', cnt)

def format_yml():
    """

        Description:
        ------------
        This function is used for formating the yml files

        Usage:
        ------
        filehandlers.format_yml()

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
    yaml.compact(seq_map=False)
    yaml.sequence_dash_offset=0
    yaml.line_break=1
    yaml.encoding='utf-8'
    #yaml.version=='%YAML 1.2'
    return yaml

def convert_jsontoyml(*argv):
    """

        Description:
        ------------
        This function is used for converting json to yml

        Usage:
        ------
        filehandlers.convert_jsontoyml('/etc/ansible/json/install-python.json','/etc/ansible/install-python.yml')

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
        yaml = format_yml()
        yaml.dump(data, out)


def convert_ymltojson(*argv):
    """

        Description:
        ------------
        This function is used for converting yml to json

        Usage:
        ------
        filehandlers.convert_ymltojson('/etc/ansible/install-python.yml','/etc/ansible/install-python.json')

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
        yaml = format_yml()
        data = yaml.load(inp)
    with open(argv[1], 'w') as out:
        json.dump(data, out, indent=2)

def convert_ymlasformatdyml(*argv):
    """

        Description:
        ------------
        This function is used for converting yml to a formatted yml 

        Usage:
        ------
        filehandlers.convert_ymlasformatdyml('/etc/ansible/json/install-python.yml','/etc/ansible/formatd/install-python.yml')

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

    with open(argv[0]) as inp:
        yaml = format_yml()
        data = yaml.load(inp)
    with open(argv[1], 'w') as out:
        yaml.dump(data, out)

def extract_pathbasename(*data):
    """

        Description:
        -----------
    """

    return os.path.basename(data[0])

def append_filetypasjson(*data):
    """

        Description:
        ------------
    """

    return os.path.splitext(data[0])[0] + '.json'

if __name__ == '__main__':
    convert_ymltojson(sys.argv[1],sys.argv[2])
