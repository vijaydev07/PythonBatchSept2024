#!/usr/bin/python3

"""
Purpose: if we update the os.path.sep value with something, will it change the behaviour of os.path.splitext

"""

import os

# splitext() is used to get the extension of file
print(os.path.splitext("user/bin/04_os_module/example.txt"))

os.path.sep = ':'
print(os.path.splitext(r"C:\user\bin\04_os_module\example.txt"))