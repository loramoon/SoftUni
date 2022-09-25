first_line, second_line = {*input().split()}, {*input().split()}
N = int(input())

for _ in range(N):
    command = input()
    nums = command.split()[2:]
    if 'Add First' in command:
        first_line = first_line.union(nums)
    elif 'Add Second' in command:
        second_line = second_line.union(nums)
    elif 'Remove First' in command:
        for num in nums:
            if num in first_line:
                first_line.remove(num)
    elif 'Remove Second' in command:
        for num in nums:
            if num in second_line:
                second_line.remove(num)
    elif 'Check Subset' in command:
        print('True' if first_line.issubset(second_line) or second_line.issubset(first_line) else 'False')

print(', '.join(map(str, sorted(map(int, first_line)))))
print(', '.join(map(str, sorted(map(int, second_line)))))
