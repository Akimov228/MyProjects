data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers = []
for i in data_tuple:
    if type(i) == str:
        letters.append(i)
    else:
        numbers.append(i)
numbers.remove(6.13)
letters.append(numbers.pop(numbers.index(True)))
numbers.insert(1, 2)
numbers.sort()
letters.reverse()
letters[1] = 'G'
letters[-2] = 'c'
multiplied_number = [element ** 2 for element in numbers]
tuple(letters)
tuple(multiplied_number)
letters_end = tuple(letters)
numbers_end = tuple(multiplied_number)

print(letters_end)
print(numbers_end)

