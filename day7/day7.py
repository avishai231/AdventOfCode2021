import numpy as np

def parse_input(filename):
    with open(filename,'r') as f:
        parsed = list(map(int,f.readline().split(',')))
    print(parsed)
    return parsed

if __name__ == '__main__':
    # read files
    inp_test = parse_input('test.txt')
    #inp = parse_input('input.txt')
    # part 1

    # part 2

