from termcolor import colored


class LabirintTurtle:
    def __init__(self, *args, **kwargs):
        self.opis = []
        self.lab = []
        self.tr = []
        self.way = -1
        self.labirint = []  # основная чистая карта
        self.turtle = []  # координаты черепашки
        self.map = 2  # состояние валидности
        self.ismap = False  # наличие карты
        self.l = []  # измененный лабиринт
        self.enter = []  # координаты выходов
        self.exit = []  # путь к выходам

    def map_l(self, *args, **kwargs):
        if l:
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
        else:
            print("Пожалуйста не запускайте функции, не относящиеся к программе")

    def load_map(self, name="", *args, **kwargs):
        try:
            file = open(name, "r")
            f = (file.read()).split("\n")
            f1 = [list(i) for i in f]
            self.labirint = f1[:len(f1) - 2]
            self.l = [[i for i in j] for j in self.labirint]
            self.lab = [[i for i in j] for j in self.labirint]
            self.map_l()
            self.l[int(f[-1])][int(f[-2])][3] = [int(f[-2]), int(f[-1])]
            self.l[int(f[-1])][int(f[-2])][0] = 0
            self.l[int(f[-1])][int(f[-2])][1] = False
            print(1)
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
                for j in range(len(i) - 1):
                    if i[j] == "🐢":
                        print(colored(i[j], "green"), end="\t")
                    else:
                        print(i[j], end="\t")
                print(i[-1])
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
                if self.turtle[1] >= h - 1 or self.turtle[0] >= w - 1 or self.turtle[0] == 0 or self.turtle[1] == 0:
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
                                self.enter.append([i, 1, i, 0])
                            else:
                                self.map = 0
                                break
                        if self.labirint[-1][i] == " ":
                            if self.labirint[-1][i - 1] != " " and self.labirint[-1][i + 1] != " ":
                                self.enter.append([i, h - 2, i, h - 1])
                            else:
                                self.map = 0
                                break
                if self.map:
                    for i in range(1, h - 1):
                        if self.labirint[i][0] == " ":
                            if self.labirint[i - 1][0] != " " and self.labirint[i + 1][0] != " ":
                                self.enter.append([1, i, 0, i])
                            else:
                                self.map = 0
                                break
                        if self.labirint[i][-1] == " ":
                            if self.labirint[i - 1][w - 1] != " " and self.labirint[i + 1][w - 1] != " ":
                                self.enter.append([w - 2, i, w - 1, i])
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
                                self.exit.append([self.l[i[1]][i[0]], i[2], i[3]])
                    if k == 0:
                        self.map = 0
                if self.map:
                    self.n_e()
                    self.map = 1
        else:
            print("Карта не была загружена.")

    # ---------------------------------------------------------------------------------------------
    def step(self, x, y, *args, **kwargs):
        try:
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
        except:
            print("Пожалуйста не запускайте функции, не относящиеся к программе")

    def wo(self, a, *args, **kwargs):
        try:
            if a % 10 == 1 and a % 100 != 11:
                return str(a) + " шаг"
            if (a % 10 == 3 or a % 10 == 2 or a % 10 == 3) and (a % 100) // 10 != 1:
                return str(a) + " шага"
            return str(a) + " шагов"
        except:
            print("Пожалуйста не запускайте функции, не относящиеся к программе")

    def n_e(self, *args, **kwargs):
        if self.map:
            for i in self.exit:
                if i[0][0] < self.way or self.way == -1:
                    self.way = i[0][0]
                    self.tr = i[0][3]
                    self.tr.append(i[1])
                    self.tr.append(i[2])

    def exit_count_step(self, *args, **kwargs):
        if self.map == 1:
            print("До ближайшего выхода", self.wo(self.way + 1))
        else:
            print("Ката не была загруженна или не является валидной")

    def exit_show_step(self, *args, **kwargs):
        if self.map == 1:
            if self.opis == []:
                self.lab[self.turtle[1]][self.turtle[0]] = "🐢"
                p = 0
                k = 0
                for i in range(1, self.way + 2):
                    x = self.tr[i * 2] - self.tr[i * 2 - 2]
                    y = self.tr[i * 2 + 1] - self.tr[i * 2 - 1]
                    if x == -1:
                        if p == 3:
                            self.opis.append("Вниз на " + self.wo(k))
                            k = 0
                        if p == 4:
                            self.opis.append("Вверх на " + self.wo(k))
                            k = 0
                        self.lab[self.tr[i * 2 + 1]][self.tr[i * 2]] = "🠔"
                        p = 1
                        k += 1
                    elif x == 1:
                        if p == 3:
                            self.opis.append("Вниз на " + self.wo(k))
                            k = 0
                        if p == 4:
                            self.opis.append("Вверх на " + self.wo(k))
                        self.lab[self.tr[i * 2 + 1]][self.tr[i * 2]] = "🠖"
                        p = 2
                        k += 1
                    elif y == 1:
                        if p == 1:
                            self.opis.append("Влево на " + self.wo(k))
                            k = 0
                        if p == 2:
                            self.opis.append("Вправо на " + self.wo(k))
                            k = 0
                        self.lab[self.tr[i * 2 + 1]][self.tr[i * 2]] = "🠗"
                        p = 3
                        k += 1
                    else:
                        if p == 1:
                            self.opis.append("Влево на " + self.wo(k))
                            k = 0
                        if p == 2:
                            self.opis.append("Вправо на " + self.wo(k))
                            k = 0
                        self.lab[self.tr[i * 2 + 1]][self.tr[i * 2]] = "🠕"
                        p = 4
                        k += 1
                if p == 1:
                    self.opis.append("Влево на " + self.wo(k))
                if p == 2:
                    self.opis.append("Вправо на " + self.wo(k))
                if p == 3:
                    self.opis.append("Вниз на " + self.wo(k))
                if p == 4:
                    self.opis.append("Вверх на " + self.wo(k))
                self.lab[self.tr[-1]][self.tr[-2]] = "🏁"
            for i in self.opis:
                print(i)
            for i in self.lab:
                for j in range(len(i) - 1):
                    if i[j] == "*" or i[j] == " ":
                        print(i[j], end="\t")
                    elif i[j] == "🏁":
                        print(colored(i[j], "red"), end="\t")
                    else:
                        print(colored(i[j], "green"), end="\t")
                if i[-1] == "🏁":
                    print(colored(i[-1], "red"))
                else:
                    print(i[-1])
        else:
            print("Ката не была загруженна или не является валидной")

