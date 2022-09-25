''''You will receive three integer numbers. Write a program that finds if their multiplication (the result)
is negative, positive, or zero. Try to do this WITHOUT multiplying the 3 numbers.'''

def product_result(a, b, c):
    if 0 in (a, b, c):
        print ('zero')
        quit()
    negative_count = 0
    for i in (a, b, c):
        if i < 0:
            negative_count+=1
    if negative_count%2!=0:
        print ('negative')
    else:
        print ('positive')
        quit()

a = int(input())
b = int(input())
c = int(input())
product_result(a, b, c)