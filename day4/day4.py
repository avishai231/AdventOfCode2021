import numpy as np

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
    # replace numbers with X
    # if count('X') on rows or columns == 5 return
    numbers = list(map(str,numbers))
    boards = np.array(boards,dtype=str)
    for num in numbers:
        for i,board in enumerate(boards):
            if num in board:
                place = np.where(board == num)
                boards[i][place[0],place[1]] = 'x'
            for j in range(5):
                if board[:,j].tolist().count('x') == 5:
                    return np.sum(process_final_board(board))*int(num)
                if board[j,:].tolist().count('x') == 5:
                    return np.sum(process_final_board(board))*int(num)
                    print(num)
                    print(board)
                    print(process_final_board(board))

if __name__ == '__main__':
    numbers, boards = parse_input('test.txt')
    result = solve1(numbers, boards)
    assert result == 4512, 'got ' + str(result) + ', expected 4512.'
    numbers, boards = parse_input('input.txt')
    result = solve1(numbers,boards)
    print(result)
