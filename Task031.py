# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

def fibonachi(n):
    if n == 1 or n == 2:
        return 1
    return fibonachi(n-1) + fibonachi(n-2)

print(fibonachi(10))
