ten = list(range(1, 10 + 1))
evens = list(filter(lambda i: i % 2 == 0 , ten))
sguare_evens = list(map(lambda i: i*i , evens))

while True:
    def out_object(seq:list = ten):
        print(seq)
        # print(ten)
        user = input('enter index: ')
        try:
            print(seq[int(user)])
        except:
            print(f'Только индексы из списка ')

        if user == 'exit':
            exit()
    out_object([1,2,3,4,3,22,3,4,55,6666,4])




# print(ten)
# print(evens)
# print(sguare_evens)