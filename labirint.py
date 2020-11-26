class LabirintTurtle:
    def __init__(self):
        self.labirint = []
        self.turtle = []
        self.map = 2
        self.ismap = False

    def load_map(self, name="", *args, **kwargs):
        try:
            file = open(name, "r")
            f = (file.read()).split("\n")
            self.labirint = f[:len(f) - 2]
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
            if self.labirint[self.turtle[0]][self.turtle[1]] == "*":
                self.map = 0
            if self.map:
                for j in self.labirint:
                    for i in j:
                        if i != " " or i != "*":
                            self.map = 0
            if self.map:
                k = 0
                if (" " not in self.labirint[0][1:w - 2:]) and (" " not in self.labirint[w - 1][1:w - 2:]):
                    for i in self.labirint[1:w - 2:]:
                        if i[0] == " " or i[w - 1] == " ":
                            k = 1
                            break
                    if not k:
                        self.map = 0


    def exit_count_step(self):
        pass

    def exit_show_step(self):
        pass


print("🐢           🐢")
print("👣           🐾")
print("👣           🐾")
print("👣           🐾")