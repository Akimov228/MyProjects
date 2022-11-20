"""ЧЕТНОЕ-НЕЧЕТНОЕ"""
# def even_odd (number):
#     if type(number) == int:
#         if number % 2 == 0:
#             return True
#         elif number % 2 != 0:
#             return False
#     else:
#         return None

# print(even_odd(1))



"""ПРАВОПИСАНИЕ НА МИНИМАЛКАХ"""
# def spelling(sentence):
#     if sentence[0] in 'QWERTYUIOPASDFGGHJKLZXCVBNMЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ' and sentence[-1] == '.':
#         return sentence
#     #     else:
#         return 'Введите предложение с заглавной буквы и поставьте точку в конце предложения!!!'
#
#
# print(spelling('Рello jwhjwjwvj.'))

"""СРЕДНЕЕ АРИФМЕТИЧЕСКОЕ"""
# def average(*args):
#         return sum(args) / len(args)
#
# print(average(1,3,11))

"""БЛИЖАЙШЕЕ ЧИСЛО"""
# def nearest(b,*a: list):
#     a = [int(i) for i in input().split()]
#     b = int(input())
#     number = 0
#     for i in range(len(a)):
#         if (b - a[i]) < b - number and b - a[i] > 0:
#             number = i
#
#
# print(nearest(2,[3,5,7]))




