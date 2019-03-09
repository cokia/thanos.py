# thanos.py

import os
import sys
import random
# arg1 = sys.argv[1]
# arg2 = sys.argv[2]
b = 0
i = 0

filelist = []
target = os.getcwd()

# def getFiles(dir):
#     x = 0
#     for pack in os.walk(dir):
#         #print( " current directory = %s , sub directory = %s  , files = %s " % ( pack[0] , pack[1],pack[2] ) )
#         for f in pack[2]:
#             x += 1
#     return x
def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            filelist.append(full_filename)
    except PermissionError:
        print("😈 Permission Error. Thanos need Root Perminssion")

# allfilecount = getFiles(target)
# halffilecount = allfilecount / 2
search(target)
random.shuffle(filelist)
print(filelist)
