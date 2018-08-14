#!/usr/bin/env python3

#https://leetcode.com/problems/longest-absolute-file-path/description/
#https://leetcode.com/problems/find-duplicate-file-in-system/description/

import os

def iterate(directory, ans):
    if directory is None:
        return ans
    max = 0
    maxPath = ""
    for path, dirs, files in os.walk(directory):
        for i in files:
            abspath = os.path.join(path,i)
            if os.path.isfile(abspath):
                f = open(abspath,"r")
                key = str(f.read()).strip('\n')
                if key not in ans.keys():
                    ans[key] = [i]
                else:
                    ans[key] += [i]
                length = len(abspath)
                if length > max:
                    max = length
                    maxPath = abspath
    print (ans)
    print (abspath)

def dfs(directory,ans):
    stack = []
    stack.append(directory)
    while len(stack) > 0:
        temp = stack.pop(len(stack) - 1)
        if (os.path.isdir(temp)):
            ans.append(temp)
            for files in os.listdir(temp):
                stack.append(os.path.join(temp,files))
        elif(os.path.isfile(temp)):
            ans.append(temp)
    print (ans)

def bfs(directory,ans):
    stack = []
    stack.append(directory)
    while len(stack) > 0:
        temp = stack.pop(0)
        if (os.path.isdir(temp)):
            ans.append(temp)
            for files in os.listdir(temp):
                stack.append(os.path.join(temp,files))
        elif(os.path.isfile(temp)):
            ans.append(temp)
    print (ans)

def main():
    hash = {}
    arr = []
    print("Iterative Method:")
    iterate("Test",hash)
    print("\nDFS Method:")
    dfs("Test",arr)
    print("\nBFS Method:")
    bfs("Test",arr)

if __name__ == '__main__':
    main()
