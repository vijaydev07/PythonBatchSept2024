#!/usr/bin/python3

"""
Purpose: To observe the diff between splitdrive and splitext methods in os module

"""

import os

# using os.path.splitext()
print(os.path.splitext("/usr/bin/os_module/test.rar"))

# using os.path.splitdrive( "on linux format path")
print(os.path.splitdrive("/usr/bin/os_module/test.rar"))

# using os.path.splitdrive( "on windows format path")
print(os.path.splitdrive(r"C:\usr\bin\os_module\test.rar"))
