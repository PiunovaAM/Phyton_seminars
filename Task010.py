# Задача 10: 
# На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть


count_coins = int(input('Введите количество монет: '))
# tails = 0
# heads = 0

for _ in range (count_coins):
    # count_coins = random.randint(0,1)
    # print(count_coins, end=' ')
    count_heads = int(input('Введите количество монет орлом вверх: '))
    print (count_coins - count_heads)





# n = int(input())
# count_zero = 0
# count_one = 0
# for i in range(n):
#     x = int(input())
#     if x == 0:
#         count_zero += 1
#     else:
#         count_one += 1
#     if count_one > count_zero:
#         print(count_zero)
#     else:
#          print(count_one)