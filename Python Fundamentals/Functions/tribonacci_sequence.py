''''In the Tribonacci sequence, every number is formed by the sum of the previous 3.
Write a function that prints numbers from the Tribonacci sequence on one line separated
by a single space, starting from 1. You will receive a positive integer number as input.
'''

num=int(input())
def tribo(num):
    new_list = [0] * num
    new_list[0] = 1
    new_list[1] = 1
    new_list[2] = 2
    for i in range(3, num):
        new_list[i]=new_list[i-3]+new_list[i-2]+new_list[i-1]
    print(*new_list,sep=" ")
if num==1:
    print(1, end="")
elif num ==0:
    print()
elif num==2:
    print("1 1", end='')
else:
    tribo(num)