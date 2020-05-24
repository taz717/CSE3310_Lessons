'''
Moataz Khallaf A.K.A Hackerman
07-heapSort
3/6/2019
'''


def heapify(arr, lenArr, rootIndex):  #  rootIndex is usually i
    # purpose is to create a max heap
    largest = rootIndex

    leftChild = 2 * rootIndex + 1
    rightChild = 2 * rootIndex + 2

    #  check if leftChild is greater than root index

    if leftChild < lenArr and arr[rootIndex] < arr[leftChild]:
        largest = leftChild

        #  check if rightChild is greater than root index

    if rightChild < lenArr and arr[largest] < arr[rightChild]:
        largest = rightChild

        #  change root value if needed

    if largest != rootIndex:
        temp = arr[rootIndex]
        arr[rootIndex] = arr[largest]
        arr[largest] = temp

        heapify(arr, lenArr, largest)

def heapSort(arr):
    #  swap last index value and index 0 of a max heap an restart the heapify proc
    lenArr = len(arr)

    # build max heap
    for i in range(lenArr, -1, -1):
        heapify(arr, lenArr, i)

    # Extract highest value and heapify again
    for i in range(lenArr - 1, 0, -1):
        temp = arr[i]
        arr[i] = arr[0]
        arr[0] = temp

        heapify(arr, i, 0)

li = [5, 17, 13, 11, 1, 7, 3 ]

heapSort(li)
print(li)