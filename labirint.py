class LabirintTurtle:
    def __init__(self):
        self.labirint = []
        self.turtle = []

    def load_map(self, name="", *args, **kwargs):
        try:
            file = open(name, "r")
            f = (file.read()).split("\n")
            self.labirint = f[:len(f) - 2]
            self.turtle.append(int(f[-2]))
            self.turtle.append(int(f[-1]))
            file.close()
        except:
            print("Файл не найден. Проверьте, правильно ли записано имя файла и его корректность.")

    def show_map(self, turtle=False):
        pass

    def check_map(self):
        pass

    def exit_count_step(self):
        pass

    def exit_show_step(self):
        pass

t = LabirintTurtle()
t.load_map("I1.txt")