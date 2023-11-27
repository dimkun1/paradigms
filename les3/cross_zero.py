# Используется объектно-ориентированная и процедурная парадигмы
# в целях возможности изменений правил и добавления в дальнейшем меню,
# дополнительных режимов и пр.
# Процедурная парадигма необходима для реализации конкретных действий игры

class Board:
    def __init__(self) -> None:
        self.area = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __str__(self) -> str:
        elem = ""
        for i in range(len(self.area)):
            if (i + 1) % 3 == 0:
                elem = elem + str(self.area[i]) + "\n"
            else:
                elem = elem + str(self.area[i]) + " "
        return elem


class Gamer:
    def __init__(self, name: str, kind: bool) -> None:
        self.name = name
        self.kind = kind

    def __str__(self) -> str:
        return self.name


class Game:
    def __init__(self, board: Board, gamer_1: Gamer, gamer_2: Gamer) -> None:
        self.board = board
        self.gamer_1 = gamer_1
        self.gamer_2 = gamer_2

    def check_field(self, step: int) -> bool:
        if step in self.board.area:
            return True
        return False

    def input_step(self, gamer: Gamer):
        if gamer.kind:
            mark = 'X'
        else:
            mark = 'O'
        step = 0
        while step == 0:
            data = input(
                f"Игрок {gamer} вводит номер поля, чтобы поставить '{mark}': ")
            if data == 'q':
                quit()
            try:
                step = int(data)
                if not step in range(1, 10):
                    raise ValueError()
            except:
                step = 0
                print('Введите корректный номер поля')
        return step, mark

    def check_win(self) -> bool:
        if self.board.area[0] == self.board.area[1] == self.board.area[2] or\
                self.board.area[3] == self.board.area[4] == self.board.area[5] or \
                self.board.area[6] == self.board.area[7] == self.board.area[8] or \
                self.board.area[0] == self.board.area[3] == self.board.area[6] or \
                self.board.area[1] == self.board.area[4] == self.board.area[7] or \
                self.board.area[2] == self.board.area[5] == self.board.area[8] or \
                self.board.area[0] == self.board.area[4] == self.board.area[8] or \
                self.board.area[2] == self.board.area[4] == self.board.area[6]:
            return True
        return False

    def play(self):
        count = 1
        print("Для выхода введите 'q'")
        while count < 10:
            print(self.board)
            if count % 2 != 0:
                gamer = self.gamer_1
            else:
                gamer = self.gamer_2
            step, mark = self.input_step(gamer)
            if self.check_field(step):
                self.board.area[step-1] = mark
                if self.check_win():
                    print(f'Победил {gamer}')
                    quit()
                count += 1
            else:
                print('Упс... Поле уже занято')
        else:
            print('Ничья, ребят...')


if __name__ == "__main__":
    name_1 = input("Введите имя игрока для 'Х': ")
    name_2 = input("Введите имя игрока для 'O': ")
    gamer_1 = Gamer(name_1, True)
    gamer_2 = Gamer(name_2, False)
    game = Game(Board(), gamer_1, gamer_2)
    game.play()