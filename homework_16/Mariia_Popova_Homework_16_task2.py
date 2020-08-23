"""
Нужно дописать основную линию сказки. Каждого героя реализовать классом с методами.
Так же должен быть класс сказки (или функция), где происходит основное действие с героями
"""

# ___________KOLOBOK_______________

from time import sleep


class Hero:
    def __init__(self, name):
        self.name = name


class Ded(Hero):
    def tell_babka_about_colobok(self):
        print("Ded asked babka to go and to scrape the box, mark the suseki, scrape flour into a Kolobok")
        sleep(1)


class Babka(Hero):
    def bake_colobok(self):
        print("Babka made everything what Ded had asked her about and put it to freeze on the window.")
        sleep(1)
        return Colobok('Kolobok')


class Colobok(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.singing = self.sing_song()
        self.running = self.run()
        self.left_home = (f'{self.name} left the home')

    def meetings(self):
        guis = ["Rabbit", "Wolf", "Bear", "Fox"]
        while True:
            for animal in guis:
                print(
                    f'{self.name} was rolling along the road and met {animal}. {animal} told {self.name} that he was going to eat him.')
                sleep(1)
                print(self.singing)
                sleep(0.5)
                if animal == "Fox":
                    print(f'Fox asked {self.name} to sit on her nose and to sing louder one more time.')
                    sleep(1)
                    print(f"{self.name} sat on the {animal}'s nose.", self.singing)
                    sleep(1)
                    print(f'Fox asked {self.name} to sit on her tongue and to sing louder one more time.')
                    sleep(1)
                    print(f"{self.name} sat on the {animal}'s tongue and {animal} ate him ")
                    sleep(1)
                    print("THE END")
                    break
                print(self.running)
                continue
            break

    def sing_song(self):
        return f'{self.name} sang a song'

    def run(self):
        return 'and run away.'


class Tale:
    def __init__(self, babka, ded):
        self.babka = babka
        self.ded = ded
        self.colobok = None

    def babkin_dom(self):
        self.ded.tell_babka_about_colobok(self.babka)
        self.colobok = self.babka.bake_colobok(self.colobok)
        self.colobok_meet = self.colobok.meetings()

    def start(self):
        self.babkin_dom()


my_tail = Tale(Babka, Ded)
print("Once upon a time there was Ded and Babka.")
sleep(1)
my_tail.babkin_dom()
