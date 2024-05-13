import re

with open('Matrix.txt', 'r') as file:
    lines = file.readlines()

firts_multiple_input = lines[0].rstrip().split()
n = int(firts_multiple_input[0])
m = int(firts_multiple_input[1])

matrix = lines[1:]
decoded_list = list(zip(*matrix))
decoded_string = ''.join([''.join(item) for item in decoded_list])

print(re.sub(r'\b[^a-zA-Z0-9]+\b', r' ', decoded_string))
