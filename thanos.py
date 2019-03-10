# thanos.py

import os
import sys
import random
arg1 = sys.argv[1]

b = 0
i = 0

filelist = []
deletelist = []
target = os.getcwd() 
target += arg1
print("[😈] Target is" + target + " !")

if (arg1 == ""):
    print("Directory is not selected! plz check and give me like thanos.py /Desktop")
    print("If u want to remove this dir, plz give me argv like thanos.py /")

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            filelist.append(full_filename)
    except PermissionError:
        print("[😈] Permission Error. Thanos need Root Perminssion")


# allfilecount = getFiles(target)

# halffilecount = allfilecount / 2
search(target)
random.shuffle(filelist)
print("[😈] Death note is ready...")
filecount = len(filelist)
for i in range(0, int(filecount / 2)):
    deletelist.append(filelist[i])
    print (deletelist[i])
print("[😈] Snapping fingers inside "+ os.getcwd() +" with full power...")
for i in range(filecount + 1):
    os.remove(str(deletelist[i]))
print("[😈] I'm done, half of files are still exist.")

