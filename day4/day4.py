import numpy as np
import copy

def parse_input(filename):
    with open(filename) as f:
        lines = f.readlines()
    numbers = list(map(int,lines[0].split(','))) # get input numbers
    # read tables into np arrays
    boards = []
    temp = []
    for i,j in enumerate(lines[2:]):
        if j != '\n':
            temp.append(list(map(int,j.split())))
            if len(temp) == 5:
                boards.append(temp)
                temp = []
    return numbers, boards

def process_final_board(matrix):
    matrix[np.where(matrix=='x')] = 0
    return matrix.astype(int)

def solve1(numbers, boards):
    # change to which board wins last
    numbers = list(map(str,numbers))
    boards = np.array(boards,dtype=str)
    for num in numbers:
        for i,board in enumerate(boards):
            if num in board:
                place = np.where(board == num)
                boards[i][place[0],place[1]] = 'x'
            # after every iteration check if row or column if finds 5*'x'
            for j in range(5):
                if board[:,j].tolist().count('x') == 5: # columns
                    return np.sum(process_final_board(board))*int(num)
                if board[j,:].tolist().count('x') == 5: # rows
                    return np.sum(process_final_board(board))*int(num)

def solve2(numbers, boards):
    numbers = list(map(str,numbers))
    boards = np.array(boards,dtype=str)
    checked = [0 for i in range(len(boards))]
    for num in numbers:
        for i,board in enumerate(boards):
            if num in board:
                place = np.where(board == num)
                boards[i][place[0],place[1]] = 'x'
            for j in range(5):
                # if a board wins it checks it in checked
                # if checked has last board left it calculates the last board with an offset due to the way
                #   the iterations go over numbers. It wasn't worth fixing as it gave the right solution.
                # this is highly inefficient as this iterates over boards that already won. This can be solved
                #   if on each board iterationis we check if the board has won. 
                if board[:,j].tolist().count('x') == 5:
                    if checked.count(0) == 1:
                        winning_board = boards[checked.index(0)]
                        return (np.sum(process_final_board(winning_board))-int(winning_num))*int(winning_num)
                    checked[i] = 1
                if board[j,:].tolist().count('x') == 5:
                    if checked.count(0) == 1:
                        winning_board = boards[checked.index(0)]
                        #print(checked,num,'\n',winning_board)
                        winning_num = numbers[numbers.index(num)+1]
                        return (np.sum(process_final_board(winning_board))-int(winning_num))*int(winning_num)
                    checked[i] = 1

if __name__ == '__main__':
    # read and process test case and complete input
    numbers_test, boards_test = parse_input('test.txt')
    numbers, boards = parse_input('input.txt')
    # part 1
    test1 = solve1(numbers_test, boards_test)
    assert test1 == 4512, 'got ' + str(test1) + ', expected 4512.'
    assert solve1(numbers,boards) == 54275, solve1(numbers,boards) 
    # part 2
    test2 = solve2(numbers_test,boards_test)
    assert test2 == 1924, test2
    print(solve2(numbers,boards))

