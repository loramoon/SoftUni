# number_list = input().split(", ")
# number_forward = ""
# number_backward = ""
# for number in number_list:
#     number_forward = number
#     number_backward = number[::-1]
#     if number_forward == number_backward:
#         print("True")
#     else:
#         print("False")

def function_poli(numbers):
    for i in numbers:
        original_number = i
        reversed_number = i[::-1]
        if original_number==reversed_number:
            print("True")
        else:
            print("False")
numbers = input().split(", ")
function_poli(numbers)