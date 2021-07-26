import sys

number = int(input())
dots = []


st_file = sys.stdin

for line in st_file:
    dots.append(list(map(int, line.split())))

print(dots)