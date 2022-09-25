text = input()

all_letters = {}

for letter in text:
    if letter not in all_letters:
        all_letters[letter] = 0
    all_letters[letter] += 1

sorted_list=sorted(all_letters.items(), key=lambda x: x[0])

for data in sorted_list:
    print(f"{data[0]}: {data[1]} time/s")

