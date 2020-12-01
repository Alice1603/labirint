class LabirintTurtle:
    def __init__(self):
        self.labirint = []  # основная чистая карта
        self.turtle = []  # координаты черепашки
        self.map = 2  # состояние валидности
        self.ismap = False  # наличие карты
        self.l = []  # измененный лабиринт
        self.enter = []  # координаты выходов
        self.exit = []  # путь к выходам

    def map_l(self):
        w = len(self.l[0])
        h = len(self.l)
        for j in range(h):
            for i in range(w):
                if self.l[j][i] != "*":
                    self.l[j][i] = [""]
                    self.l[j][i].append(True)
                    self.l[j][i].append(True)
                    self.l[j][i].append([])
                    if j == 0 or i == 0 or i == w - 1 or j == h - 1:
                        self.l[j][i] = "*"

    def load_map(self, name="", *args, **kwargs):
        try:
            file = open(name, "r")
            f = (file.read()).split("\n")
            f1 = [list(i) for i in f]
            self.labirint = f1[:len(f1) - 2]
            self.l = [[i for i in j] for j in self.labirint]
            self.map_l()
            self.l[int(f[-1])][int(f[-2])][3] = [int(f[-1]), int(f[-2])]
            self.l[int(f[-1])][int(f[-2])][0] = 0
            self.l[int(f[-1])][int(f[-2])][1] = False
            self.turtle.append(int(f[-2]))
            self.turtle.append(int(f[-1]))
            file.close()
            self.ismap = True
            self.check_map()
            print("Карта успешно загружена")
        except:
            print(
                "Файл не найден или не соответствует небходимому формату.\nПроверьте, правильно ли записано имя файла "
                "и его корректность.")

    def show_map(self, turtle=False, *args, **kwargs):
        if self.ismap and self.map == 1:
            if turtle:
                a = self.labirint[self.turtle[1]][self.turtle[0]]
                self.labirint[self.turtle[1]][self.turtle[0]] = "🐢"
            for i in self.labirint:
                print(*i)
            if turtle:
                self.labirint[self.turtle[1]][self.turtle[0]] = a
        else:
            print("Ката не была загруженна или не является валидной")

    def check_map(self, *args, **kwargs):
        if self.ismap:
            if self.map == 1:
                print("Карта является валидной")
            elif not self.map:
                print("Карта не соответствует условиям валидности.")
            else:
                w = len(self.labirint[0])
                h = len(self.labirint)
                # проверка на позицию черепашки
                if self.turtle[1] > h - 1 or self.turtle[0] > w - 1:
                    self.map = 0
                if self.labirint[self.turtle[1]][self.turtle[0]] == "*" and self.map:
                    self.map = 0
                # проверка символов
                if self.map:
                    for j in self.labirint:
                        for i in j:
                            if i != " " and i != "*":
                                self.map = 0
                                break
                # проверка на прямоугольность карты
                if self.map:
                    for i in self.labirint:
                        if len(i) != w:
                            self.map = 0
                            break
                if self.map:
                    for i in range(1, w - 1):
                        if self.labirint[0][i] == " ":
                            if self.labirint[0][i - 1] != " " and self.labirint[0][i + 1] != " ":
                                self.enter.append([i, 1])
                            else:
                                self.map = 0
                                break
                        if self.labirint[-1][i] == " ":
                            if self.labirint[-1][i - 1] != " " and self.labirint[-1][i + 1] != " ":
                                self.enter.append([i, w - 2])
                            else:
                                self.map = 0
                                break
                if self.map:
                    for i in range(1, h - 1):
                        if self.labirint[i][0] == " ":
                            if self.labirint[i - 1][0] != " " and self.labirint[i + 1][0] != " ":
                                self.enter.append([1, i])
                            else:
                                self.map = 0
                                break
                        if self.labirint[i][-1] == " ":
                            if self.labirint[i - 1][h - 1] != " " and self.labirint[i + 1][h - 1] != " ":
                                self.enter.append([h - 2, i])
                            else:
                                self.map = 0
                                break
                if not self.enter and self.map:
                    self.map = 0
                # поиск пути
                if self.map:
                    self.step(self.turtle[0], self.turtle[1])
                # проверка на замкнутость
                k = 0
                if self.map:
                    for i in self.enter:
                        if self.l[i[1]][i[0]] != "*":
                            if not self.l[i[1]][i[0]][2]:
                                k += 1
                                self.exit.append(self.l[i[1]][i[0]])
                    if k == 0:
                        self.map = 0
                if self.map:
                    self.map = 1
        else:
            print("Карта не была загружена.")

    # ---------------------------------------------------------------------------------------------
    def step(self, x, y):
        a = self.l[y][x]
        i = 1
        a[1] = False
        # вниз
        while self.l[y + i][x] != "*":
            s = self.l[y + i][x]
            if (not s[0] and s[0] != 0) or (s[0] - i >= a[0]):
                s[0] = a[0] + i
                s[3] = [j for j in self.l[y + i - 1][x][3]]
                s[3].append(x)
                s[3].append(y + i)
            i += 1
        i = 1
        # вправо
        while self.l[y][x + i] != "*":
            s = self.l[y][x + i]
            if (not s[0] and s[0] != 0) or (s[0] - i >= a[0]):
                s[0] = a[0] + i
                s[3] = [j for j in self.l[y][x + i - 1][3]]
                s[3].append(x + i)
                s[3].append(y)
            i += 1
        i = 1
        # влево
        while self.l[y][x - i] != "*":
            s = self.l[y][x - i]
            if (not s[0] and s[0] != 0) or (s[0] - i >= a[0]):
                s[0] = a[0] + i
                s[3] = [j for j in self.l[y][x - i + 1][3]]
                s[3].append(x - i)
                s[3].append(y)
            i += 1
        i = 1
        # вверх
        while self.l[y - i][x] != "*":
            s = self.l[y - i][x]
            if (not s[0] and s[0] != 0) or (s[0] - i >= a[0]):
                s[0] = a[0] + i
                s[3] = [j for j in self.l[y - i + 1][x][3]]
                s[3].append(x)
                s[3].append(y - i)
            i += 1
        if self.l[y - 1][x] != "*":
            if self.l[y - 1][x][1]:
                self.step(x, y - 1)
        if self.l[y][x - 1] != "*":
            if self.l[y][x - 1][1]:
                self.step(x - 1, y)
        if self.l[y + 1][x] != "*":
            if self.l[y + 1][x][1]:
                self.step(x, y + 1)
        if self.l[y][x + 1] != "*":
            if self.l[y][x + 1][1]:
                self.step(x + 1, y)
        a[2] = False
        return 0

    def exit_count_step(self):
        if self.map:
            mi = -1
            w = []
            for i in self.exit:
                if i[0] < mi or mi == -1:
                    mi = i[0]
                    w = i[3]
            print("До ближайшего выхода", mi + 1, "шагов.")

    def exit_show_step(self):
        pass


l = LabirintTurtle()
l.load_map("L1.txt")
print()
print()
print()
print()
print("🐢           🐢")
print("👣           🐾")
print("👣           🐾")
print("👣           🐾")
