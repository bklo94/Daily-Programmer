#!/usr/bin/env python3
import os
import time
#n*7 operations to swap contents of file
def swap(a,b,dict):
    temp = dict[a]
    f = open(a,"w")
    f.write(dict[b])
    f.close()
    f = open(b,"w")
    f.write(temp)
    f.close()

def getFiles(directory):
    if not directory:
        print("Error: Directory not found")
        return
    dict = {}
    arr = []
    for path, dirs, files in os.walk(directory):
        for i in sorted(files):
            abspath = os.path.join(path,i)
            if os.path.isfile(abspath):
                f = open(abspath,"r")
                dict[abspath] = f.read()
                arr.append(abspath)
    i = 0
    j = len(dict.keys())-1
    while(i < j):
        swap(arr[i],arr[j],dict)
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
