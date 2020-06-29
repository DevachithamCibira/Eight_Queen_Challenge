

class EightQueens():
    def __init__(self):
        self.CB_list = [0, 0, 0, 0, 0, 0, 0, 0]
        self.final_list = []
        self.queen_moves = []
        self.queen_locat = []
        self.moves_possible = []
        self.level_1 = []
        self.level_2 = []
        self.level_3 = []
        self.level_4 = []
        self.level_5 = []
        self.level_6 = []
        self.level_7 = []
        self.level_8 = []




    def Run(self):
        self.working()


    def end_result(self):
        final_result = ""
        for value in self.final_list[0]:
            final_result = final_result + " " + str(value)
        final_result = final_result[1:]
        return final_result


    def working(self):
        count = 0
        self.Queen_moves()

        for move in self.moves_possible:
            if move[1] == 1:
                self.level_1.append(move)
        for _ in range(len(self.level_1)):
            move_1 = self.level_1.pop(0)
            self.CB_list[0] = move_1[0]
            self.board()
            for move in self.moves_possible:
                if move[1] == 2:
                    self.level_2.append(move)
            for _ in range(len(self.level_2)):
                move_2 = self.level_2.pop(0)
                self.CB_list[1] = move_2[0]
                self.board()
                for move in self.moves_possible:
                    if move[1] == 3:
                        self.level_3.append(move)
                for _ in range(len(self.level_3)):
                    move_3 = self.level_3.pop(0)
                    self.CB_list[2] = move_3[0]
                    self.board()

                    for move in self.moves_possible:
                        if move[1] == 4:
                            self.level_4.append(move)
                    for _ in range(len(self.level_4)):
                        move_4 = self.level_4.pop(0)
                        self.CB_list[3] = move_4[0]
                        self.board()
                        for move in self.moves_possible:
                            if move[1] == 5:
                                self.level_5.append(move)
                        for _ in range(len(self.level_5)):
                            move_5 = self.level_5.pop(0)
                            self.CB_list[4] = move_5[0]
                            self.board()

                            for move in self.moves_possible:
                                if move[1] == 6:
                                    self.level_6.append(move)
                            for _ in range(len(self.level_6)):
                                move_6 = self.level_6.pop(0)
                                self.CB_list[5] = move_6[0]
                                self.board()
                                for move in self.moves_possible:
                                    if move[1] == 7:
                                        self.level_7.append(move)
                                for _ in range(len(self.level_7)):
                                    move_7 = self.level_7.pop(0)
                                    self.CB_list[6] = move_7[0]
                                    self.board()
                                    for move in self.moves_possible:
                                        if move[1] == 8:
                                            self.level_8.append(move)
                                    for _ in range(len(self.level_8)):
                                        move_8 = self.level_8.pop(0)
                                        self.CB_list[7] = move_8[0]
                                        self.board()

                                    if 0 not in self.CB_list:
                                        count = count + 1
                                        #print(CB_list)
                                        temp = []
                                        for val in self.CB_list:
                                            val = val - 1
                                            temp.append(val)
                                        self.final_list.append(temp[:])

                                    self.CB_list[7] = 0
                                self.CB_list[6] = 0
                            self.CB_list[5] = 0
                        self.CB_list[4] = 0
                    self.CB_list[3] = 0
                self.CB_list[2] = 0
            self.CB_list[1] = 0
        print(count)


    def Queen_moves(self):

        self.queen_locat, self.queen_moves, self.moves_possible, self.moves = [], [], [], []
        [[self.moves_possible.append((row, col)) for col in range(1, 9)] for row in range(1, 9)]
        for i in range(8):
            if self.CB_list[i] != 0:
                self.queen_locat.append((self.CB_list[i], i + 1))
        for queen_position in self.queen_locat:
            for i in range(1, 9):
                self.queen_moves.append((queen_position[0], i))
                self.queen_moves.append((i,queen_position[1]))
                if queen_position[0] - i > 0 and queen_position[1] + i > 0:
                    self.queen_moves.append((queen_position[0] - i, queen_position[1] - i))
                if queen_position[0] + i < 9 and queen_position[1] + i < 9:
                    self.queen_moves.append((queen_position[0] + i, queen_position[1] + i))
                if queen_position[0] - i > 0 and queen_position[1] + i < 9:
                    self.queen_moves.append((queen_position[0] - i, queen_position[1] + i))
                if queen_position[0] + i < 9 and queen_position[1] - i > 0:
                    self.queen_moves.append((queen_position[0] + i, queen_position[1] - i))
            self.queen_moves = list(dict.fromkeys(self.queen_moves))
        [self.moves_possible.remove(move) for move in self.queen_moves if move in self.moves_possible]


    def board(self):
        self.Queen_moves()



if __name__ == '__main__':
    my_queen = EightQueens()
    my_queen.Run()
    print((my_queen.end_result()))
    print(my_queen.final_list)
    [print(val) for val in my_queen.final_list[0]]


