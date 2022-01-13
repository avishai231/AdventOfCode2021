def count_inc(filename):
    with open(filename,'r') as f:
        lines = f.readlines()
    inc = 0; dec = 0
    for i,j in enumerate(lines[1:]):
        if int(j) > int(lines[i]):
            inc += 1
#    print('increase:', inc)
    return(inc)

def sliding_window_3(filename):
    with open(filename,'r') as f:
        lines = f.readlines()
    lines = [int(n) for n in lines]
    inc = 0
    sums = []
    for i,j in enumerate(lines[:-2]):
        sums.append(lines[i] + lines[i+1] + lines[i+2])
    for i in range(len(sums[:-1])):
        if sums[i] < sums[i+1]: inc += 1
    return inc

if __name__ == '__main__':
    assert count_inc('test.txt') == 7, count_inc('test.txt')
    assert sliding_window_3('test.txt') == 5, sliding_window_3('test.txt')
    print(count_inc('day1_input.txt'))
    print(sliding_window_3('day1_input.txt'))
