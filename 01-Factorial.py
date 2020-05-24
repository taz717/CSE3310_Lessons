'''
Moataz Khallaf A.K.A Hackerman
01-Factorial
2/26/2019
'''

#f(x) = f * f(x-1)

def getFactorial(num):
    #base case
    if num == 1:
        return 1
    else:
        return num * getFactorial(num - 1)

print(getFactorial(7))