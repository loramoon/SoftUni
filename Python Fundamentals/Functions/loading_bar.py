# def loading_bar(number):
#     load_bar = "[]"
#     idx = number // 10
#     for i in range(1, idx + 1):
#         load_bar = load_bar[:i] + "%" + load_bar[i:]
#     load_bar = load_bar[:idx + 1] + (10 - idx) * "." + load_bar[idx + 1:]
#     if number == 100:
#         return f"100% Complete!\n{load_bar}"
#     else:
#         return f"{number}% {load_bar}\nStill loading..."
#
#
# current_number = int(input())
# print(loading_bar(current_number))

def loading_bar(n):
    ready = ("%"*int(n/10))
    remain = ("."*int(10-n/10))
    loading_bar = ready+remain
    return loading_bar

n = int(input())
if n==100:
    print(f'100% Complete!\n[{loading_bar(n)}]')
else:
    print(f'{n}% [{loading_bar(n)}]\nStill loading...')

'''You will receive a single integer number between 0 and 100 (inclusive)
divisible by 10 without remainder (0, 10, 20, 30...). 
Your task is to create a function that returns a loading bar depending on 
the number you have received in the input. Print the result on the console. 
For more clarification, see the examples below.
50% [%%%%%.....]
Still loading...
100% Complete!
[%%%%%%%%%%]
'''