from string import punctuation
line_number = 0

with open('even_lines.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    while True:
        line = input_file.readline()
        if not line:
            break
        line_number += 1
        letters = len([x for x in line if x.isalpha()])
        marks = len([x for x in line if x in punctuation])
        output_file.write(f'Line {line_number}: {line[:-1]} ({letters})({marks})\n')
        # output_file.write(f'Line {line_number}: {line.strip()} ({letters})({marks})\n')