# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции
def sum_odd_index(lst):
    sum = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            sum += lst[i]
    print(f"Сумма равна: {sum}")
lst = list(map(int, input("Введите числа через пробел: ").split()))
sum_odd_index(lst)