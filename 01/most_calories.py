#!/usr/bin/env python3


with open('input') as f:
    lines = f.readlines()

totals = [0]
index = 0

for line in lines:
    if line == '\n':
        index += 1
        totals.append(0)
    else:
        totals[index] += int(line.strip())

totals.sort()
# Top Elf
print(f'Top Elf {totals[-1]}')
# Sum of top 3
print(f'Sum of top 3 {totals[-1]+totals[-2]+totals[-3]}')
