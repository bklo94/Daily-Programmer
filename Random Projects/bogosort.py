import random
import time

target = list("Hello, World")
arr = [""] * len(target)
i = 0

while i < len(target):
    arr[i] = chr(random.randint(32,126))
    if arr[i] == target[i]:
        i+= 1
    print("".join(arr))
    time.sleep(0.005)
