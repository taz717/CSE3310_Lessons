'''
Moataz Khallaf A.K.A Hackerman
03-recuBinSearch
2/27/2019
'''
import random

li = [1, 2, 3, 4, 5, 15, 16, 17, 18, 19, 20, 30, 31, 32, 33, 34, 35, 36, 41, 42, 43, 43]
dat = []

for i in range(500):

    if random.randrange(2) == 1:
        dat.append(i)

num = dat[random.randrange(len(dat))]

def binSearch(arr, value):
    midpoint = len(arr)//2
    if arr[midpoint] == value:
        return arr[1]
    else:
        if arr[midpoint] < value:
            arr = arr[midpoint:]
        else:
            arr = arr[:midpoint]
        return binSearch(arr, value)



print(binSearch(dat, num))

''' Mr.Zhang's method
def recBinSearch(li, val)
    mid = (len(li)-1)//2
    if li[midP] == val:
        return li[midP]
    if val < li[midP]:
        return recBinSearch(li[:midP])
    else: val > li[midP]:
        return recBinSearch(li[midP+1:])



'''