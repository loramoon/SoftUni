def find_negative_positive_sum(*args):
    positive_sum = 0
    negative_sum = 0
    for el in args:
        if el < 0:
            negative_sum += el
        else:
            positive_sum += el
    return positive_sum, negative_sum


nums = [int(x) for x in input().split()]
positive_sum, negative_sum = find_negative_positive_sum(*nums)
print(negative_sum)
print(positive_sum)
if abs(positive_sum)>abs(negative_sum):
    print(f"The positives are stronger than the negatives")
else:
    print(f"The negatives are stronger than the positives")