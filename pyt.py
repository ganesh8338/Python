#!/usr/bin/python
import subprocess
def uname_fun():
	uname = "uname"
	uname_arg = "-a"
print("Gatering system information with %s command:\n"%uname)
subprocess.call([uname,uname_arg])
