from random import randint, choice, randrange
from enum import Enum


class SuperAbility(Enum):
    HEAL = 1
    CRITICAL_DAMAGE = 2
    BOOST = 3
    SAVE_DAMAGE_AND_REVERT = 4
    TAKE_HP_GIVE_HERO = 5
    GOLEMS_POWER = 6
    SURIKENS = 7
    BIG_DAMAGE = 8


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.name} health: {self.health} damage: {self.damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super(Boss, self).__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        random_hero = choice(heroes)
        self.__defence = random_hero.super_ability

    def attack(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.health = hero.health - self.damage

    def __str__(self):
        return 'BOSS ' + super(Boss, self).__str__() + f' defence: {self.defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, super_ability):
        super(Hero, self).__init__(name, health, damage)
        self.__super_ability = super_ability

    @property
    def super_ability(self):
        return self.__super_ability

    def attack(self, boss):
        boss.health = boss.health - self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super(Warrior, self).__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        coefficient = randint(2, 5)
        boss.health = boss.health - coefficient * self.damage
        print(f'Warrior hits critically {coefficient * self.damage}')


class Magic(Hero):
    def __init__(self, name, health, damage):
        super(Magic, self).__init__(name, health, damage, SuperAbility.BOOST)

    def apply_super_power(self, boss, heroes):
        pass


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super(Medic, self).__init__(name, health, damage, SuperAbility.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and self != hero:
                hero.health = hero.health + self.__heal_points


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super(Berserk, self).__init__(name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)
        self.__saved_damage = 0

    def apply_super_power(self, boss, heroes):
        pass

class Hacker(Hero):
    def __init__(self, name, health, damage):
        super(Hacker, self).__init__(name, health, damage, SuperAbility.TAKE_HP_GIVE_HERO)

    def apply_super_power(self, boss, heroes):
        taked_hp = randrange(30, 40, 5)
        for hero in heroes:
            if self != hero:
                boss.health = boss.health - taked_hp
                random_hero1 = choice(heroes)
                random_hero1.health = random_hero1.health + taked_hp
        print(f'Hacker taked out {taked_hp} health and give it to {random_hero1.name} ')


class Golem(Hero):
    def __init__(self, name, health, damage):
        super(Golem, self).__init__(name, health, damage, SuperAbility.GOLEMS_POWER)

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero != self:
                self.health -= int(boss.damage * 0.2)
        print(f'Golem got {int(boss.damage * 0.2)} of damage')


class Samurai(Hero):
    def __init__(self, name, health, damage):
        super(Samurai, self).__init__(name, health, damage, SuperAbility.SURIKENS)

    def apply_super_power(self, boss, heroes):
        virus = randrange(20, 40, 10)
        boss.health = boss.health - virus
        vaccine = randrange(20, 30, 5)
        boss.health = boss.health + vaccine

        surikens = [vaccine, virus]

        random_suriken = choice(surikens)
        print(f'Samurai chose suriken of {random_suriken} ')

class Minion(Hero):
    def __init__(self, name, health, damage):
        super(Minion, self).__init__(name, health, damage, SuperAbility.BIG_DAMAGE)

    def apply_super_power(self, boss, heroes):
        coeficient = randint(2, 4)
        boss.health = boss.health - self.damage * coeficient
        print(f'Minion hits critically {coeficient * self.damage}')
        """?????????? ?????????? - ????????????, ?????????? ?????????????? ???????? , ???? ???????????? ???????????????? .
        ???????????????? ?????????????????????? ???????????????????????? ?????????? ???? ??????????,
        ???? ???????? ???????? ???????????????????? ???? ?????????????????? ??????????????????????"""


round_number = 0


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True

    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
    return all_heroes_dead


def start_game():
    boss = Boss('Tanos', 2200, 80)
    warrior = Warrior('Harrold', 280, 10)
    doc = Medic('Haus', 250, 5, 15)
    magic = Magic('Hendelf', 270, 15)
    berserk = Berserk('Kratos', 260, 20)
    assistant = Medic('Strange', 290, 10, 5)
    hacker = Hacker('Jeff', 250, 10)
    golem = Golem('Gollem', 400, 5)
    samurai = Samurai('Segun', 270, 0)
    minion = Minion('Mitano', 100, 80)

    heroes = [warrior, doc, magic, berserk, assistant, hacker, golem, samurai, minion]

    print_statistics(boss, heroes)

    while not is_game_finished(boss, heroes):
        play_round(boss, heroes)


def print_statistics(boss, heroes):
    print('ROUND ' + str(round_number) + ' ------------')
    print(boss)
    for hero in heroes:
        print(hero)


def play_round(boss, heroes):
    global round_number
    round_number += 1
    if boss.health > 0:
        boss.choose_defence(heroes)
        boss.attack(heroes)
    for hero in heroes:
        if hero.health > 0 and boss.health > 0 and boss.defence != hero.super_ability:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)
    print_statistics(boss, heroes)


start_game()
