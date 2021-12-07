
the_numbers = []
the_board = []

def populate_boards():
    global the_numbers
    global the_board
    with open('04-1-input.txt') as f:
        line = f.readline()
        the_numbers = [int(x) for x in line.split(',')]
        print(the_numbers)
        line = f.readline()

        while line:
            if line[0] != '\n':
                some_nums = (line.strip()).split()
                the_board = the_board + [int(x) for x in some_nums]
            line = f.readline()

    print(the_board)


def print_winning_score(board_num, num):
    idx_start = board_num * 25
    the_sum = 0
    for idx in range(idx_start,idx_start+25):
        if the_board[idx] < 100:
            the_sum += the_board[idx]
    print(the_sum, num, the_sum*num)

def mark_boards():
    global the_numbers
    global the_board
    num_of_boards = int(len(the_board) / 25)
    row_and_col_cnt = 5*num_of_boards
    the_rows = [0] * row_and_col_cnt
    the_columns = [0] * row_and_col_cnt
    the_winners = []

    for num in the_numbers:
        for idx, spot in enumerate(the_board):
            if num == spot:
                the_board[idx] = spot + 100
                board_num = int(idx / 25)
                board_pos = idx % 25
                row_num = int(board_pos/5)
                col_num = board_pos%5
                row_idx = board_num * 5 + row_num
                col_idx = board_num * 5 + col_num
                the_rows[row_idx] += 1
                the_columns[col_idx] += 1
                if board_num not in the_winners:
                    if the_rows[row_idx] == 5:
                        print("BINGO!", board_num, the_rows[row_idx], row_idx)
                        the_winners.append(board_num)
                        print_winning_score(board_num, num)
                    if the_columns[col_idx] == 5:
                        the_winners.append(board_num)
                        print("BINGO!", board_num, the_columns[col_idx], col_idx)
                        print_winning_score(board_num, num)

    print(the_board)

if __name__ == '__main__':
    populate_boards()
    mark_boards()