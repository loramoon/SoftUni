file = open('./even_lines.txt')
line_number = 0
symbols = ["-", ",", ".", "!", "?"]

while True:
    line = file.readline()
    if not line:
        break

    if line_number % 2 == 0:
        for row in line:
            for symbol in symbols:
                line = line.replace(symbol, '@')
        print(*line.split()[::-1])

    line_number += 1

file.close()