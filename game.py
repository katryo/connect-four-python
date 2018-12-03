from itertools import repeat


Y = 0
R = 1

INVALID = 0
CONTINUE = 1
END = 2
TIE = 3


class Game:
    def __init__(self):
        self.board = [[' '] * 7 for _ in range(6)]
        self.current_player = Y

    def _is_end_move(self, row, idx):
        def is_out(r, c):
            if r < 0 or c < 0 or r > len(self.board)-1 or c > len(self.board[0])-1:
                return True
            return False

        def count_target(r_iter, c_iter):
            count = 0
            for r, c in zip(r_iter, c_iter):
                if is_out(r, c):
                    break
                if self.board[r][c] == target:
                    count += 1
                    continue
                else:
                    break
            return count

        if self.current_player == Y:
            target = 'Y'
        else:
            target = 'R'

        count = -1
        count += count_target(repeat(row), range(idx, idx+4))
        count += count_target(repeat(row), range(idx, idx-4, -1))
        if count >= 4:
            return True

        count = -1
        count += count_target(range(row, row+4), repeat(idx))
        count += count_target(range(row, row-4, -1), repeat(idx))
        if count >= 4:
            return True

        count = -1
        count += count_target(range(row, row+4), range(idx, idx+4))
        count += count_target(range(row, row-4, -1), range(idx, idx-4, -1))
        if count >= 4:
            return True

        count = -1
        count += count_target(range(row, row+4), range(idx, idx-4, -1))
        count += count_target(range(row, row-4, -1), range(idx, idx+4))
        if count >= 4:
            return True

        return False

    def _is_filled(self):
        for r in self.board:
            for cell in r:
                if cell == ' ':
                    return False
        return True

    def play_move(self, idx):
        assert 0 <= idx <= 6
        if self.board[0][idx] != ' ':
            return INVALID # filled

        if self.current_player == Y:
            token = 'Y'
        else:
            token = 'R'

        filled_row = -1
        for i in range(5, -1, -1):
            if self.board[i][idx] == ' ':
                self.board[i][idx] = token
                filled_row = i
                break

        if self._is_end_move(filled_row, idx):
            return END
        if self._is_filled():
            return TIE
        return CONTINUE

    def show_board(self):
        print('---------------')
        for row in self.board:
            print('|'.join(row))
        print('---------------')

    def play(self):
        while True:
            self.show_board()
            line = input().strip()
            try:
                index = int(line)
            except:
                print("Invalid input. Please try again")
                continue
            result = self.play_move(index)
            if result == INVALID:
                print("Invalid index. Please try again")
                continue
            elif result == CONTINUE:
                if self.current_player == Y:
                    self.current_player = R
                else:
                    self.current_player = Y
                continue
            elif result == END:
                self.show_board()
                if self.current_player == Y:
                    print("Yellow won!")
                    return
                else:
                    print("Red won!")
                    return
            else:
                print("Tie")
                return


if __name__ == '__main__':
    game = Game()
    game.play()