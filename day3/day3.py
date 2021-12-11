import numpy as np
import copy

def parse_input(filename):
    with open(filename,'r') as f:
        lines = f.readlines()
    matrix = [] 
    for line in lines:
        matrix.append([i for i in line[:-1]])
    return np.array(matrix,dtype=int)

def solve(mat):
    line_len = len(mat[0,:])
    gamma = ''; epsilon = ''
    for i in range(line_len):
        common = np.bincount(mat[:,i]).argmax()
        if common == 1:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    return int(gamma,2)*int(epsilon,2)

def solve2(mat):
    result = ''
    line_len = len(mat[0,:])
    len_mat = len(mat)
    #while len_mat > 1:
    mat_ox = copy.deepcopy(mat)
    mat_co = copy.deepcopy(mat)
    for i in range(line_len):
        if len(mat_ox) > 1:
            counter_ox = np.bincount(mat_ox[:,i])
            common_ox = counter_ox.argmax()
            if counter_ox[0] == counter_ox[1]:
                common_ox = 1
            mat_ox = mat_ox[mat_ox[:,i] == common_ox, :]
        if len(mat_co) > 1:
            counter_co = np.bincount(mat_co[:,i])
            common_co = counter_co.argmin()
            if counter_co[0] == counter_co[1]:
                common_co = 0
            mat_co = mat_co[mat_co[:,i] == common_co, :]
    conv_mat = [2**i for i in range(line_len-1,-1,-1)]
    print(np.sum(conv_mat*mat_ox))
    ox = ''.join([str(i) for i in np.ndarray.tolist(mat_ox[0])])
    co = ''.join([str(i) for i in np.ndarray.tolist(mat_co[0])])
    return int(ox,2)*int(co,2)

if __name__ == '__main__':
    test1 = parse_input('test.txt')
    assert solve(test1) == 198, "got " + str(solve(test1)) + " expected 198"
    input = parse_input('input.txt')
    print(solve(input))
    assert solve2(test1) == 230, "got " + str(solve2(test1)) + " expected 230"
    print(solve2(input))
