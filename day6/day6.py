import numpy as np

def parse_input(filename):
    with open(filename,'r') as f:
        output = np.array(list(map(int,f.readline().split(','))))
    return output

def update_state(state):
    new_state = state - 1
    add8 = np.count_nonzero(new_state < 0)
    new_state[new_state < 0] = 6
    return np.append(new_state,add8*[8])

assert update_state(np.array([3,4,3,1,2])).tolist() == [2,3,2,0,1]
assert update_state(np.array([2,3,2,0,1])).tolist() == [1,2,1,6,0,8]

def solve1(initial_state,n):
    #print('Initial state:', initial_state)
    state = update_state(initial_state)
    for i in range(1,n):
        #print('After % day:' % (i), state)
        state = update_state(state)
    return len(state)

def update_list(input):
    grow = input[0]
    state = input[1:] + [grow]
    state[6] += grow
    return state

assert update_list([0,1,1,2,1,0,0,0,0]) == [1,1,2,1,0,0,0,0,0]

def solve2(initial_state,n):
    ist = initial_state.tolist()
    # convert input into occurance list:
    state = [0,0,0,0,0,0,0,0,0]
    for i in initial_state:
        state[i] += 1
    # update state in steps
    for i in range(n):
        state = update_list(state)
    return sum(state)

if __name__ == '__main__':
    # read inputs
    initial_test = parse_input('test.txt')
    #assert initial_test.tolist() == [3,4,3,1,2], initial_test
    initial = parse_input('input.txt')

    # part 1
    test1 = solve1(initial_test,80)
    assert test1 == 5934, test1
    assert solve1(initial,80) == 361169, 'Correct solution'
    # part 2
    test2 = solve2(initial_test,80)
    #print(test2)
    assert test2 == 5934, test2
    assert solve2(initial,80) == 361169
    assert solve2(initial_test,256) == 26984457539
    print(solve2(initial,256))
