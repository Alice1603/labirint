class LabirintTurtle:
    def __init__(self):
        self.labirint = []
        self.turtle = []
        self.map = 2
        self.ismap = False
        self.l = []

    def load_map(self, name="", *args, **kwargs):
        try:
            file = open(name, "r")
            f = (file.read()).split("\n")
            f1 = [list(i) for i in f]
            self.labirint = f1[:len(f1) - 2]
            self.l = [[list(i) for i in j] for j in self.labirint]
            self.l[int(f[-2])][int(f[-1])] = [0]
            self.l[int(f[-2])][int(f[-1])].append(False)
            self.l[int(f[-2])][int(f[-1])].append(True)
            self.l[int(f[-2])][int(f[-1])].append([int(f[-2]), int(f[-1])])
            self.turtle.append(int(f[-2]))
            self.turtle.append(int(f[-1]))
            file.close()
            self.ismap = True
        except:
            print("Файл не найден или не соответствует небходимому формату.\nПроверьте, правильно ли записано имя файла и его корректность.")

    def show_map(self, turtle=False):
        if self.ismap and self.map == 1:
            if turtle:
                a = self.labirint[self.turtle[0]][self.turtle[1]]
                self.labirint[self.turtle[0]][self.turtle[1]] = "🐢"
            for i in self.labirint:
                print(*i)
            if turtle:
                self.labirint[self.turtle[0]][self.turtle[1]] = a
        else:
            print("Ката не была загруженна или не является валидной")


    def check_map(self):
        if self.ismap:
            w = len(self.labirint[0])
            h = len(self.labirint)
            if self.turtle[0] > h or self.turtle[1] > w:
                self.map = 0
                print(1)
            if self.labirint[self.turtle[0]][self.turtle[1]] == "*" and self.map:
                self.map = 0
                print(2)
            if self.map:
                for j in self.labirint:
                    for i in j:
                        if i != " " and i != "*":
                            self.map = 0
                            print(3)
                            break
            if self.map:
                k = 0
                if (" " not in self.labirint[0][1:w - 2:]) and (" " not in self.labirint[w - 1][1:w - 2:]):
                    for i in self.labirint[1:w - 2:]:
                        if i[0] == " " or i[w - 1] == " ":
                            k = 1
                            break
                    if not k:
                        self.map = 0
                        print(4)
            if self.map:
                self.map = 1
        else:
            print("Карта не была загружена.")

    def step(self, x, y):
        a = self.l[y][x]
        if self.l[y][x + 1] != "*" and self.l[y][x + 1][1]:
            self.l[y][x + 1] = a[0] + 1


    def exit_count_step(self):
        pass

    def exit_show_step(self):
        pass


l = LabirintTurtle()
l.load_map("hhbbj")
l.check_map()
l.show_map()
l.load_map("L1.txt")
l.check_map()
l.show_map()
print()
print()
print()
print()
print("🐢           🐢")
print("👣           🐾")
print("👣           🐾")
print("👣           🐾")