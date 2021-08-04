message = input("Введите зашифрованное сообщение: ") 
temp = 0
part_1 = ''
part_2 = ''
for symbol in message:
  temp += 1
  if temp % 2 != 0:
    part_1 = part_1 + symbol
  elif temp % 2 == 0:
    part_2 = symbol + part_2
print("Расшифрованное сообщение: ", part_1+part_2)