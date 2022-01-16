"""
Description of what this file does.
"""

printEnabled = True

def xprint(*args, mode="Log", **kwargs):
    if(printEnabled):
        print(mode+": "+"".join(map(str,args)), **kwargs)