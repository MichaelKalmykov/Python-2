# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное
binary_number = ""
num = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))
while num != 0:
    binary_number += str(num%2)
    num //=2
print(binary_number)