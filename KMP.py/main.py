# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

t = 'амневсепохуйясделанизмясалилилавыывфафыаитидмддипоху'

p = [0] * len(t)

j = 0
i = 1

while i < len(t):
    if t[j] == t[i]:
        p[i] = j + 1
        i += 1
        j += 1
    else:
        if j == 0:
            p[i] = 0
            i += 1
        else:
            j = p[j-1]
print(p)
