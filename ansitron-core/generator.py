#! /usr/bin/python3

def get_var_value(filename="varstore.dat"):
    with open(filename, "a+") as f:
        f.seek(0)
        v = float(f.read()) + 0.1
        #val = '{0:.2g}'.format(val)
        val = format(v,".2f")
        f.seek(0)
        f.truncate()
        f.write(val)
        return val

def main():
    get_var_value()

