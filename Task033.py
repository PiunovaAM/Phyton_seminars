# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.


list_1 = [5, 4, 2, 2, 4, 2, 2, 5]
min_ = min(list_1)
max_ = max(list_1)
list_2 = [min_ if i == max_ else i for i in list_1]
print(list_2)


# list_1 = [5, 4, 2, 2, 4, 2, 2, 5]
# min_ = min(list_1)
# max_ = max(list_1)
# list_2 = [max_ if i == min_ else i for i in list_1]
# print(list_2)


