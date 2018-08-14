#!/usr/bin/env python3
import os
import time
#n*3 operations to swap files
def swap(a,b):
    os.rename(a,a+".tmp")
    os.rename(b,a)
    os.rename(a+".tmp",b)

def getFiles(directory):
    if not directory:
        print("Error: Directory not found")
        return
    arr = []
    for path, dirs, files in os.walk(directory):
        for i in sorted(files):
            abspath = os.path.join(path,i)
            if os.path.isfile(abspath):
                arr.append(abspath)
    i = 0
    j = len(arr)-1
    while(i < j):
        swap(arr[i],arr[j])
        i+=1
        j-=1

def main():
    getFiles("/home/bklo/Documents/Test/Test/")

#time in milliseconds
if __name__ == '__main__':
    t0 = time.clock()
    main()
    t1 = time.clock()
    total = t1-t0
    print (total*1000)
