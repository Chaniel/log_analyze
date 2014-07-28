#!/usr/bin/python
#Date: 2013-06-21
#Purpose: analyze logs, to get the total number of imsi

import os
import re
import string
import glob
import fileinput
import sys
import os
import shutil


# to find files , store into filelist[]

filelist = []
log = glob.glob('log')
filelist.extend(log)

"""
filelist = []
#filelist = list(os.system('find /data/w-applogs/ -type f -name "hserver.log.20130630*"'))
log1 = glob.glob('/data/server.log.20130630*')
log2 = glob.glob('/data/server.log.20130630*')
filelist.extend(log1)
filelist.extend(log2)
"""

print filelist


#if the value of the key that you want to find exists, then call this def, return the value of the key.
def find_value(line, key):
        list1 = line.split(key)
#       print list1
        list2 = list1[1].split(' ')
#       print list2

        list3 = list2[0].split('=')
#       print list3[1]

        value = list3[1]
#       print value
        return value

# to determin if the line contains imsi, if match return 0, else return 1.
def ismatch_imsi(str1):
#       reg1 = re.compile('.*=\d{15} .*')
#        reg1 = re.compile('.*imsi=\d{15} .*')
        reg1 = re.compile('\d{11}')
        match1 = reg1.match(str1)
	print match1
        if match1 != None:
                return 0
        else:
                return 1


#reg1 = re.compile('')
#reg1 = re.compile('^\d{15}$')
#reg1 = re.compile('.*=\d{15} .*')

imsi_list = []
print imsi_list
#with open('logs/server.log.20130607095027') as f:

for file in filelist:
        with open(file) as f:
                for line in f:
                        print line
                        if ismatch_imsi(line) == 0: 
                        	
				#imsi_list.append();
				 imsi_list.append(find_value(line,'imsi'))

#print imsi_list
#to get the number of imsi_list, the total number of imsi
numb = len(set(imsi_list))

# write the result to file
with open ('num', 'w') as n:
        n.write(str(numb))
        n.write('\n')
