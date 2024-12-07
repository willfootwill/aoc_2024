import re

text = open("input/day3").read()

pattern = r'\bmul\((\d+),(\d+)\)'

matches = re.findall(pattern, text)

matches_list_multiplied = [(int(num1) * int(num2)) for num1, num2 in matches]

print(sum(matches_list_multiplied))