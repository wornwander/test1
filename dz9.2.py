class ручка:
    def __init__(self, цвет, чернила):
        self.цвет = цвет
        self.чернила = чернила

    def писать(self):
        if self.чернила > 0:
            print("ручка пишет", self.цвет, "цветом")
            self.чернила -= 1
        else:
            print("чернила закончились")

    def заправить(self, сколько):
        self.чернила += сколько
        print("ручка заправлена на", сколько)

    def показать_чернила(self):
        print("осталось чернил:", self.чернила)

р = ручка("синим", 3)
р.писать()
р.писать()
р.показать_чернила()
р.заправить(2)
р.писать()


#2


class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print("имя:", self.name, "| возраст:", self.age)

p1 = person("некет", 14)
p2 = person("авраам", 15)
p3 = person("гриша", 13)
p4 = person("боря", 14)
p5 = person("артём", 16)

people = [p1, p2, p3, p4, p5]

for p in people:
    p.show_info()