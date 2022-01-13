def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
        commands = [(k.split()[0],int(k.split()[1])) for k in lines]
    return(commands)

def update_pos(command_list):
    depth = 0; horiz = 0; aim = 0
    for i in command_list:
        if i[0] == 'forward': horiz += i[1]
        if i[0] == 'up': depth += i[1]
        if i[0] == 'down': depth -= i[1]
    return abs(depth)*horiz

def update_pos2(command_list):
    depth = 0; horiz = 0; aim = 0
    for i in command_list:
        if i[0] == 'forward':
            horiz += i[1]
            depth += aim*i[1]
        if i[0] == 'up':
            aim -= i[1]
        if i[0] == 'down':
            aim += i[1]
    return abs(depth)*horiz


if __name__ == '__main__':
    #print(read_file('test.txt'))
    final_pos = update_pos(read_file('test.txt'))
    assert final_pos == 150, 'got ' + str(final_pos) + ' expected 150'
    final_pos2 = update_pos2(read_file('test.txt'))
    assert final_pos2 == 900, 'got ' + str(final_pos) + ' expected 900'
    print(update_pos(read_file('input.txt')))
    print(update_pos2(read_file('input.txt')))

