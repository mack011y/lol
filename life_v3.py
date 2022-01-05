import pygame

Size = 700
sc = pygame.display.set_mode([Size, Size])

class Cell():
    life: int

    def __init__(self, life):
        self.life = life

    def get_life(self):
        return self.life

    def change(self, life):
        self.life = life

class Screen():
    cells: [[]]

    def __init__(self, size):
        self.size = size
        self.cells = [[Cell(0) for i in range(size)] for j in range(size)]

    def change(self, i, j, is_life):
        self.cells[i][j].change(is_life)

    def iteration(self):
        v_change_position = [[0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        temporary_cells = [[Cell(0) for i in range(self.size)] for j in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                count = 0
                for ch in v_change_position:
                    new_i = i + ch[0]
                    new_j = j + ch[1]
                    if (new_i < 0 or new_i >= 100 or new_j < 0 or new_j >= 100):
                        continue
                    else:
                        if self.cells[new_i][new_j].get_life():
                            count += 1
                if (self.cells[i][j].get_life()):
                    if count == 2 or count == 3:
                        temporary_cells[i][j].change(1)
                elif (count == 3):
                    temporary_cells[i][j].change(1)
        temporary_cells, self.cells = self.cells, temporary_cells

    def print(self):
        List_Of_Color = ['#ff0000', '#ffa500', '#ffff00', '#008000', '#42aaff', '#0000ff', '#8b00ff']
        sc.fill(pygame.Color('black'))
        for i in range(self.size):
            for j in range(self.size):
                if self.cells[i][j].get_life():
                    pygame.draw.rect(sc, pygame.Color(List_Of_Color[abs(i - j) % 7]), (i * 7, j * 7, 7, 7))
                else:
                    pygame.draw.rect(sc, pygame.Color('black'), (i * 7, j * 7, 7, 7))
        pygame.display.flip()
        pygame.time.wait(200)

def main():
    screen = Screen(100)

    for i in range(screen.size):
        for j in range(screen.size):
            if i % 3 != 0:
                screen.change(i, j, 1)

    while (1):
        screen.print()
        screen.iteration()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

if __name__ == '__main__':
    main()
