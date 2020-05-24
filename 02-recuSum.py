'''
Moataz Khallaf A.K.A Hackerman
02-recuSum
2/26/2019
'''

def getSum(li):
    #what is the base case?
    #when list has 1 value
    if len(li) == 1:
        return li[0]
    #how to simplify to the base case?
    else:
        return li[0] + getSum(li[1:])


    #something to do with the list data structure

aList = [ 1, 3, 5, 7, 11, 13, 17, 19, 23]

print(getSum(aList))