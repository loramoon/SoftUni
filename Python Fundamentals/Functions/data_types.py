type_data = input()
data = input()

def types(command, s):
    if command == 'int':
        index = int(s)
        result = index * 2
        print(result)
    elif command == 'real':
        index = float(s)
        result = index * 1.5
        print(f'{result:.2f}')
    elif command == 'string':
        print(f'${s}$')


types(type_data, data)


'''Write a function that, depending on the first line of the input, reads one of the following strings: "int", "real", or "string".
•	If the data type is an int, multiply the number by 2.
•	If the data type is real, multiply the number by 1.5 and format the result to the second decimal point.
•	If the data type is a string, surround the input with "$".
Print the result on the console.
'''