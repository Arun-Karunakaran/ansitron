#! /usr/bin/python3

import os, hashlib, sys

#__all__=['licensecheck','md5sum']

os.environ['MY_PACKAGE_ROOT'] = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
licfilenm = os.path.join(os.environ['MY_PACKAGE_ROOT'], 'LICENSE.md')
licensed_addresses = [b'O\x05\x9bK7[.7\x10\xa9\x99\xa9\xa7\xd6\xa5\x0f',b'O\x05\x9bK7[.7\x10\xa9\x99\xa9\xa7\xd6\xa5']

def _md5sum(licfilenm, blocksize=None):

    try:
        hash = hashlib.md5()
        with open(licfilenm, "rb") as f:
            for block in iter(lambda: f.read(blocksize), b""):
                hash.update(block)
        return hash.digest(), hash.hexdigest()
    except FileNotFoundError:
        print('License File Not Found')
        sys.exit()

def _licensecheck(func):

    try:
        rt1, rt2 = func()
        #print(bytes(rt1, 'utf-8'))
        #rt3 = str(rt1, 'utf-16')
        #rt3 = ctypes.c_ubyte.from_buffer_copy(bytes(str(rt1, 'utf-16'), 'utf-8')).value
        #print (rt3)
        if (int.from_bytes(rt1[:16], "big") - int.from_bytes(bytes(rt2[:16], encoding='utf-8'), "big")).to_bytes(16, byteorder='big') in licensed_addresses:
            return 'License check passed'
            pass
            #start application
        else:
            return 'License check failed. Add a valid license'
            #sys.exit()
    except UnicodeDecodeError:
        return 'License check failed'

def main():

    __license__ = (_licensecheck(lambda: _md5sum(licfilenm, 65536)))
    if __license__ != 'License check passed':
        print('License check failed. Add a valid license')
        sys.exit()
    else:
        print('License check passed')
        sys.exit()

