# def is_perfect_number(n):
#     return "We have a perfect number!" \
#         if n == sum(x for x in range(1, n)
#                     if n % x == 0) \
#         else "It's not so perfect."
#
# print(is_perfect_number(int(input())))

def perfect_number(num):
    prop_div = 0
    for n in range(1, num):
        if num % n == 0:
            prop_div += n
    if prop_div == num:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")
    return num


number = int(input())
perfect_number(number)



''''A perfect number is a positive integer that is equal to the sum of its proper positive divisors.
That is the sum of its positive divisors, excluding the number itself (also known as its aliquot sum).
Write a function that receives an integer number and returns one of the following messages:
•	"We have a perfect number!" - if the number is perfect.
•	"It's not so perfect." - if the number is NOT perfect.
Print the result on the console.
'''