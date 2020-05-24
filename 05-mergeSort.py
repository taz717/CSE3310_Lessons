'''
Moataz Khallaf A.K.A Hackerman
05-mergeSort
3/4/2019
'''

def mergeSort(li):
    if len(li) > 1:
        # split array into smaller pieces
        mid = len(li)//2
        leftHalf = li[:mid]
        rightHalf = li[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i = 0
        j = 0
        k = 0

        # Arrange arrays of 1 value in correct order

        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                li[k] = leftHalf[i]
                i += 1
            else:
                li[k] = rightHalf[j]
                j += 1
            k += 1

        # Append remainder of leftSide list if rightSide is done

        while i < len(leftHalf):
            li[k] = leftHalf[i]
            i += 1
            k += 1

        # Append remainder of rightSide if leftSide is done

        while j < len(rightHalf):
            li[k] = rightHalf[j]
            j += 1
            k += 1

    return li

aList = [5, 17, 13, 11, 1, 7, 3]

newList = mergeSort(aList)
print(newList)




