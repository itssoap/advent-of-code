import string
import re

lines = []

with open("aoc1.txt", "r") as f:
    lines = f.readlines()

sum = 0

for line in lines:
    temp = re.findall("[0123456789]", line)
    sum += int(temp[0] + temp[-1])

print(sum)

