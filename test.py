#
# demo to start os command
#
from subprocess import check_output

cmd = r'C:\cygwin64\bin\ps.exe'
output = check_output(cmd)
print (output)


