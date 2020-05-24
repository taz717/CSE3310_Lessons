'''
Moataz Khallaf A.K.A Hackerman
04-bonusRecu
2/27/2019
'''

### !!! 1 !!! ###
def getSum(li):
    if len(li) == 1:
        return li[0]
    else:
        return li[0] + getSum(li[1:])

### !!! 2 !!! ###
def getMin(li):
    if len(li) == 1:
        return li[0]
    else:
        if li[0] > li[1]:
            li.pop(0)
        else:
            li.pop(1)
    return getMin(li)

li = [1,12,13,15,2]

print(getMin(li))