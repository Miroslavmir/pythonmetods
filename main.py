# 9.183. Даны два предложения.
# Напечатать слова, которые встречаются в двух предложениях только один раз.
# s = input('введите предложения: ')
# s2 = ''
# for i in s.rstrip('.').split():
#      if s.count(i) == 1: s2 += ' ' + i
# print(s2)

# l = []
# for i in 'Trixie is best pony pony'.split():
#      if i in l:
#           l.remove(i)
# else: l.append(i)
# print(i)

# 9.182. Даны два предложения.
# Напечатать слова, которые есть только в одном из
# них (в том числе повторяющиеся)
# s = input().split(" ")
# p = input().split(" ")
# s = ["abc", "de", "db", "gc", "gc"]
# p = ["abd", "db", "bc", "bc", "db"]
#
# for i in s:
#      if i not in p:
#           print(i)
#
# for i in p:
#      if i not in s:
#           print(i)
# a = 'new year letter is comig'
# b = 'new year  letter'
# for i in a.split(' '):
#      if a.count(i) == 1:
#           print(i)
# for i in b.split(' '):
#      if b.count(i) == 1:
#           print(i)
# 8.54.*Дано натуральное число n. Получить все простые делители этого числа.
import random
# n = int(input('введите число: '))
# for i in range(2, n):
#      if n % i == 0:
#           print(i, end = '')

# 11.245.*Дан массив. Переписать его элементы в другой массив такого же размера
# следующим образом: сначала должны идти все отрицательные элементы,
# а затем все остальные. Использовать только один проход по исходному
# массиву. сумма матриц массива

matrix = []
summa = 0

for i in range(5):
     matrix.append([random.randint(-10, 10) for i in range(5)])
     print(matrix[i])
     summa += matrix[i][i]
     print(matrix[i][i], end = ' ')
