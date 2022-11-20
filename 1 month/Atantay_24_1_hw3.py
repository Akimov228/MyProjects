while True:
    word = input('введите слово: ').lower()
    if word == 'exit':
        break
    print(f'Количество букв: {len(word)}')
    count = 0
    glas = 'ауоыиэяюёеaeiouАУОЫИЭЯЁЕAEIOU'
    for i in word:
            if i in glas:
                count += 1
    print(f'Количество гласных: {count}')
    count1 = 0
    sogl = 'йцкнгшщзхъфвпрлджчсмтьбqwrtpsdfghjklzxcvbnmЙЦКНГШЩЗХФВПРЛДЖЪЧСМТЬБQWRTPSDFGHJKLZXCVBNM'
    for i in word:
        if i in sogl:
            count1 += 1
    print(f'Количество согласных: {count1}')
    print(f'Гласные/Согласные: {round(count / len(word) * 100, 2)}% /', f'{round(count1 / len(word) * 100 ,2)}%')

