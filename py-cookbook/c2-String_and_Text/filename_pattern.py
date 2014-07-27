from fnmatch import fnmatch
import os

files = os.listdir('/home/tracyliang/code/tmp/shell_test/')
print files
print [f for f in files if fnmatch(f, 'data??.csv')]


