print('Ты загадываешь число от 1 до 100\nА я попытаюсь найти!')
print("Если цифра больше, чем ты загадал пиши '>' \nЕсли цифра меньше, чем ты загадал пиши '<'")
low = 0
high = 100
c = 0
with open('result.txt', 'a', encoding="utf-8") as a:
    while True:
        try:
            number = int(input("Введите число, которое вы загадали!: "))
        except ValueError:
            print('Введите число от 1 до 100')
            continue
        sred = (high + low) // 2
        c += 1
        if sred == number:
            print(f'Я отгадал с {c} попытки!\nЭто число {number}!')
            a.write(f'Я отгадал с {c}-попытки\nЭто число {number}!')
            break
        print(f"Вы загадали {str(sred)}? ")
        check_ans = input()
        if check_ans == '<':
            high = sred
            sred = (high + low) // 2
        elif check_ans == '>':
            low = sred
            sred = (high + low) // 2
        else:
            print("Допустимы знаки: <,>\n")

