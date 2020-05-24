'''
Moataz Khallaf A.K.A Hackerman
06-2QuickSort
3/5/2019
'''

li = [5, 17, 13, 11, 1, 7, 3]

def partition(li, first, last):
    pivotVal = li[first]

    leftMark = first + 1
    rightMark = last

    done = False
    while not done:

        while leftMark <= rightMark and li[leftMark] <= pivotVal:
            leftMark += 1

        while rightMark >= leftMark and li[rightMark] >= pivotVal:
            rightMark -= 1

        if rightMark < leftMark:  # stopping case in iteration itself
            done = True

        else:
            temp = li[leftMark]
            li[leftMark] = li[rightMark]
            li[rightMark] = temp

    temp = li[first]
    li[first] = li[rightMark]  #li[first], li[rightMark] = li[rightMark], li[first]
    li[rightMark] = temp

    return rightMark

def quickSort(li, first, last):
    if first < last:  # stopping case
        splitPoint = partition(li, first, last)

        quickSort(li, first, splitPoint -1)
        quickSort(li, splitPoint +1, last)


li = [5, 17, 13, 11, 1, 7, 3]
quickSort(li, 0, len(li)-1)
print(li)