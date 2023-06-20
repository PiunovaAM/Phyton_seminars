# Задача №11. 
# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

fibo_1, fibo_2  = 0, 1
fibo_n = int(input('Введите число Фибоначчи: '))
index = 1
while fibo_2 < fibo_n:
    fibo_1, fibo_2 = fibo_2, fibo_1 + fibo_2
    index += 1
print(index if fibo_n == fibo_2 else -1)



# fibonachiLi = int(input("Введите число: "))
# result = -1
# fib_sum = 0
# temp = 0
# temp2 = 1
# index = 0
# print(index)
# while fib_sum <= fibonachiLi:
#     fib_sum = temp + temp2
#     temp = temp2
#     temp2 = fib_sum
#     index += 1

# if (temp == fibonachiLi):
#     print(index)
# else:
#     print(result)