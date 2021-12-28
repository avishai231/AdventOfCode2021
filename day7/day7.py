import numpy as np

def parse_input(filename):
    with open(filename,'r') as f:
        parsed = list(map(int,f.readline().split(',')))
    return parsed

def solve1(positions):
    min_pos = min(positions); max_pos = max(positions)
    solution = sum(positions)
    pos = np.array(positions)
    for i in range(min_pos, max_pos):
        calc = sum(abs(pos - i))
        if calc < solution:
            solution = calc
    return solution

def solve2(positions):
    # This solution works but is highly inefficient, takes ~19s
    min_pos = min(positions); max_pos = max(positions)
    pos = np.array(positions)
    solution = sum([abs(sum(range(abs(j-0)+1))) for j in pos])
    for i in range(1, max_pos):
        # instead of simple "-i" implement some kind of power law or series?
        calc = sum([abs(sum(range(abs(j-i)+1))) for j in pos])
        if calc < solution:
            solution = calc
    return solution

if __name__ == '__main__':
    # read files
    inp_test = parse_input('test.txt')
    inp = parse_input('input.txt')
    # part 1
    test1 = solve1(inp_test)
    assert test1 == 37, test1
    assert solve1(inp) == 331067, 'Verified solution'
    # part 2
    print(solve2(inp_test))
    test2 = solve2(inp_test)
    assert test2 == 168, test2
    print(solve2(inp))

