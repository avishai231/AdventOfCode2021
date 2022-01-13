import numpy as np

# This is decryption problem

def parse_input(filename):
    with open(filename,'r') as f:
        lines = f.readlines()
    clues  = [i.split('|')[0].split() for i in lines]
    digits = [i.split('|')[1].split() for i in lines]
    return clues, digits 

def solve1(clues,digits):
    numbers_counter = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    for i in digits:
        numbers_counter[1] += len(list(filter(lambda x: len(x)==2,i)))
        numbers_counter[4] += len(list(filter(lambda x: len(x)==4,i)))
        numbers_counter[7] += len(list(filter(lambda x: len(x)==3,i)))
        numbers_counter[8] += len(list(filter(lambda x: len(x)==7,i)))
    return sum(numbers_counter.values())

def decA(clue):
    # this should be incorporated into decoder but it's not worth the time
    #print(clue)
    num1 = list(filter(lambda x: len(x)==2,clue))[0]
    num7 = list(filter(lambda x: len(x)==3,clue))[0]
    for i in num1:
        num7 = num7.replace(i,'')
    return num7

def code_break(clue):
    d = {}
    d['a'] = decA(clue)
    num1 = list(filter(lambda x: len(x)==2,clue))[0]
    num4 = list(filter(lambda x: len(x)==4,clue))[0]
    num7 = list(filter(lambda x: len(x)==3,clue))[0]
    cand_bd = num4; cand_cf = num7
    for i in num7:
        cand_bd = cand_bd.replace(i,'')
    for i in num1:
        cand_bd = cand_bd.replace(i,'')
    cand_cf = cand_cf.replace(d['a'],'')
    num235 = list(filter(lambda x: len(x)==5,clue))
    for i,j in enumerate(num235):
        num235[i] = num235[i].replace(d['a'],'').replace(cand_bd[0],'').replace(cand_bd[1],'').replace(cand_cf[0],'').replace(cand_cf[1],'')
    d['g'] = min(num235,key=len) 
    d['e'] = max(num235,key=len).replace(d['g'],'')
    num069 = list(filter(lambda x: len(x)==6,clue))
    num9 = [w for w in num069 if set(w) >= set(cand_bd+cand_cf)][0]
    num069.remove(num9) # now only 06

    num6 = [w for w in num069 if set(w) >= set(cand_bd)][0]
    num069.remove(num6) # now only 0
    num0 = num069[0]

    for i in d['a']+d['e']+d['g']+cand_bd:
        num6 = num6.replace(i,'')
    d['f'] = num6  # wrong
    d['c'] = cand_cf.replace(d['f'],'')
    for i in d['a']+d['c']+d['f']+d['e']+d['g']:
        num0 = num0.replace(i,'')
    d['b'] = num0
    num8 = list(filter(lambda x: len(x)==7,clue))[0]
    for i in d.values():
        num8 = num8.replace(i,'')
    d['d'] = num8
    return d

code = ['acedgfb','cdfbe','gcdfa','fbcad','dab','cefabd','cdfgeb','eafb','cagedb','ab']
examp = ['cdfeb','fcadb','cdfeb','cdbaf']
def decoder(keys,num):
    num = [''.join(sorted(n)) for n in num]
    num_map = {'abcefg':'0','cf':'1','acdeg':'2','acdfg':'3','bcdf':'4','abdfg':'5','abdefg':'6','acf':'7','abcdefg':'8','abcdfg':'9'}
    new_map = {}
    for i in num_map:
        temp = ''
        for j in i:
            temp += keys[j]
        new_map[''.join(sorted(temp))] = num_map[i]
    new_num = ''
    for i in num:
        new_num += new_map[i]
    return new_num

#decoder(code_break(code,d={}),examp)
assert decoder(code_break(code),examp) == '5353'

def solve2(clues,digits):
    total_sum = 0
    for i,j in enumerate(clues):
        d = code_break(j)
        total_sum += int(decoder(code_break(j),digits[i]))
    return total_sum

if __name__=='__main__':
    inp_test = parse_input('test.txt')
    inp = parse_input('input.txt')

    # part 1
    test1 = solve1(inp_test[0],inp_test[1])
    assert test1 == 26, test1
    #print(solve1(inp[0],inp[1]))

    # part 2
    test2 = solve2(inp_test[0],inp_test[1])
    assert test2 == 61229, test2
    print(solve2(inp[0],inp[1]))

