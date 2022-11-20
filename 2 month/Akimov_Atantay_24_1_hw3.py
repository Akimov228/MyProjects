class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        self.__memory += 128

    def __str__(self):
        return f'Процессор: {self.cpu} память: {self.memory}'

    def __gt__(self, other):
        return self.memory > other.memory

    def __lt__(self, other):
        return self.memory < other.memory

    def __eq__(self, other):
        return self.memory == other.memory

    def __ge__(self, other):
        return self.memory >= other.memory

    def __le__(self, other):
        return self.memory <= other.memory

    def __ne__(self, other):
        return self.memory != other.memory

class Phone:
    def __init__(self, sim_card_list):
        self.__sim_card_list = sim_card_list

    @property
    def sim_card_list(self):
        return self.__sim_card_list

    @sim_card_list.setter
    def sim_card_list(self, value):
        self.__sim_card_list = value

    def call(self, sim_card_number, call_to_number):
        print(f'Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {self.sim_card_list}')

    def __str__(self):
        return f'Список сим карт: {self.sim_card_list}'

class SmartPhone(Computer,Phone):
    def __init__(self, cpu, memory, sim_card_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_card_list)

    def use_gps(self, location):
        print(f'Маршрут до {location} построен')

    def __str__(self):
        return super().__str__() + f' ' + f'Список сим-карт: {self.sim_card_list}'







Acer = Computer('amd', 512)
Nokia = Phone(('beeline', "mega", 'O!'))
Iphone = SmartPhone('IOS', 256, 'beeline')
Samsung = SmartPhone('Android', 256, 'beeline')
print(Acer)
print(Nokia)
print(Iphone)
print(Samsung)
Acer.make_computations()
Nokia.call(1, 7090907004)
Iphone.call(2, 7088804844)
Iphone.use_gps('Osh')
Samsung.call(2, 7155515151)
Samsung.use_gps('Bishkek')

