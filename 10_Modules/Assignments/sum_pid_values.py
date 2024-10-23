#!/usr/bin/python3

"""
Purpose: Summation of process id vales

"""

import os
import sys
import subprocess

#os.system('ls -ltr')

#output = subprocess.Popen('ps -ef '.split())

p = subprocess.Popen('ps -ef'.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(type(p))
output, error = p.communicate()
output = output.decode('utf-8')
print(type(output))

lines = output.splitlines()
pids = []
for line in lines[1:]:  # Skip the header line
    columns = line.split()
    if columns:  # Ensure there are columns
        pid = columns[1]  # PID is usually in the second column
        pids.append(int(pid))

print(sum(pids))