import numpy as np

def parse_input(filename):
    with open(filename) as f:
        lines = f.readlines()
        lines = [line.strip('\n') for line in lines]
    return lines

def check_line(line):
    # find corrupted lines!
    starts  = ['(','[','{','<']
    endings = [')',']','}','>']
    stack = []
    for i in line:
        if i in starts:
            stack.append(i)
        elif i in endings:
            pos = endings.index(i)
            if len(stack) > 0 and starts[pos] == stack[len(stack)-1]:
                stack.pop()
            else:
                stack.append(i)
                return "corrupted",stack
    if len(stack) == 0:
        return "balanced",stack
    else:
        return "unbalanced",stack

assert check_line('([])')[0] == 'balanced'
assert check_line('{()()()}')[0] == 'balanced'
assert check_line('<([{}])>')[0] == 'balanced'
assert check_line('[<>({}){}[([])<>]]')[0] == 'balanced'
assert check_line('(((((((((())))))))))')[0] == 'balanced'
assert check_line('(]')[0] == 'corrupted'
assert check_line('{()()()>')[0] == 'corrupted'
assert check_line('(((()))}')[0] == 'corrupted'
assert check_line('[{[{({}]{}}([{[{{{}}([]')[0] == 'corrupted'
assert check_line('{([(<{}[<>[]}>{[]{[(<()>')[0] == 'corrupted'
assert check_line('[[<[([]))<([[{}[[()]]]')[0] == 'corrupted'
assert check_line('[<(<(<(<{}))><([]([]()')[0] == 'corrupted'
assert check_line('<{([([[(<>()){}]>(<<{{')[0] == 'corrupted'

def solve1(filename):
    lines = parse_input(filename)
    corruption_level = 0
    for i in lines:
        result = check_line(i)
        #if result[0] == 'corrupted':
            #print(result[0],i,result[1][-1])
        if result[1][-1] == ')':
            corruption_level += 3
        if result[1][-1] == ']':
            corruption_level += 57
        if result[1][-1] == '}':
            corruption_level += 1197
        if result[1][-1] == '>':
            corruption_level += 25137
    print(corruption_level)

def solve2(filename):
    lines = parse_input(filename)
    starts  = ['(','[','{','<']
    endings = [')',']','}','>']
    scores = []
    for i in lines:
        line_score = 0
        result = check_line(i)
        if result[0] == 'unbalanced':
            joined = ''.join(reversed(result[1]))
            t = ''
            for i in joined:
                pos = starts.index(i)
                t += endings[pos]
            for i in t:
                line_score *= 5
                if i == ')': line_score += 1
                if i == ']': line_score += 2
                if i == '}': line_score += 3
                if i == '>': line_score += 4
            scores.append(line_score)
            #print(line_score)
    scores.sort()
    print(scores[len(scores)//2])
    return scores[len(scores)//2]
#assert solve2('test.txt') == 288957

#solve1('test.txt')
#solve1('input.txt')
solve2('test.txt')
solve2('input.txt')
