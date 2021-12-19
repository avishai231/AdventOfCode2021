import numpy as np

def parse_input(filename):
    # find maximum number
    with open(filename) as f:
        lines = f.readlines()
        lines = [l.strip('\n') for l in lines]
        lines = [i.split(' -> ') for i in lines]
    for i,j in enumerate(lines):
        lines[i] = [k.split(',') for k in j]
    moves = np.array(lines,dtype=int) 
    map_size = np.max(moves)
    return map_size, moves

def solve1(map_size, moves):
    # 1. create map, maybe as a dictionary with keys as coordiantes?
    # 2. apply moves on map
    map = np.zeros([map_size+1,map_size+1])
    for i in moves:
        # moving up-down
        if i[0][0] == i[1][0]:
            move_range = (i[0][1],i[1][1])
            movements = list(range(min(move_range),max(move_range)+1))
            for j in movements:
                map[i[0][0],j] += 1
        # moving left-right
        if i[0][1] == i[1][1]:
            move_range = (i[0][0],i[1][0])
            movements = list(range(min(move_range),max(move_range)+1))
            for j in movements:
                map[j,i[0][1]] += 1
    return np.count_nonzero(map>1)

def solve2():
    return


if __name__ == '__main__':
    # read inputs
    inp_test = parse_input('test.txt')
    inp = parse_input('input.txt')
    # part 1
    assert inp_test[0] == 9, inp_test
    test1 = solve1(inp_test[0],inp_test[1])
    assert test1 == 5, test_1
    print(solve1(inp[0],inp[1]))
    #assert test1 == , test1
    # part 2
    # test2 = solve2()
    # assert test2 == , test2
    
