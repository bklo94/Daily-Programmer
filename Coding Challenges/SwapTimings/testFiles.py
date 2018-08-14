#!/usr/bin/env python3
import os
import csv
#generates the files
def generateFiles(n):
    for i in range(1,n+1):
        os.chdir("/home/bklo/Documents/Test/Test/")
        file = open(str(i).zfill(7),"w")
        file.write(str(i).zfill(7))
        file.close()

def main():
    seed = 500
    trials = 250
    cmd = "make clean && make"
    os.system(cmd)
    print("Starting Trials")
    for i in range(0, trials):
        generateFiles(seed)
        os.chdir("/home/bklo/Documents/Test/")
        cmd = "./swap.py >> pySwap.csv"
        os.system(cmd)
    print("Completed PySwap")
    for i in range(0, trials):
        generateFiles(seed)
        os.chdir("/home/bklo/Documents/Test/")
        cmd = "./swapRenaming.py >> pyRenaming.csv"
        os.system(cmd)
    print("Completed PyRenaming")
    for i in range(0, trials):
        generateFiles(seed)
        os.chdir("/home/bklo/Documents/Test/")
        cmd = "./cswap >> cswap.csv"
        os.system(cmd)
    print("Completed cswap")
    for i in range(0, trials):
        generateFiles(seed)
        os.chdir("/home/bklo/Documents/Test/")
        cmd = "./cswapRenaming >> cswapRenaming.csv"
        os.system(cmd)
    print("Completed cswapRenaming")
    for i in range(0, trials):
        generateFiles(seed)
        os.chdir("/home/bklo/Documents/Test/")
        cmd = "./cswapRenamingOpt  >> cswapRenamingOpt.csv"
        os.system(cmd)
    print("Completed cswapRenamingOpt")
    for i in range(0, trials):
        generateFiles(seed)
        os.chdir("/home/bklo/Documents/Test/")
        cmd = "./pcswap >> pcswap.csv"
        os.system(cmd)
    print("Completed pcswap")
    for i in range(0, trials):
        generateFiles(seed)
        os.chdir("/home/bklo/Documents/Test/")
        cmd = "./pcswapRenaming >> pcswapRenaming.csv"
        os.system(cmd)
    print("Completed pcswapRenaming")
    for i in range(0, trials):
        generateFiles(seed)
        os.chdir("/home/bklo/Documents/Test/")
        cmd = "./pcswapRenamingOpt >> pcswapRenamingOpt.csv"
        os.system(cmd)
    print("Completed pcswapRenamingOpt")



if __name__ == '__main__':
    main()
