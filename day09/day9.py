import numpy as np

def parse_input(filename):
    with open(filename,'r') as f:
        lines = f.readlines()
    mat = [[int(i) for i in line.strip('\n')] for line in lines]
    return np.array(mat)

def solve1(mat):
    total = 0
    # check corners
    if mat[0][0]<mat[0][1] and   mat[0][0]<mat[1][0]: total += mat[0][0]+1            #top left
    if mat[0][-1]<mat[0][-2] and mat[0][-1]<mat[1][-1]: total += mat[0][-1]+1       #top right
    if mat[-1][0]<mat[-1][1] and mat[-1][0]<mat[-2][0]: total += mat[-1][0]+1       #bot left
    if mat[-1][-1]<mat[-1][-2] and mat[-1][-1]<mat[-2][-1]: total += mat[-1][-1]+1  #bot right
        
    for i,j in enumerate(mat[0][1:-1]): # middle numbers of top row
        if j<mat[0][i] and j<mat[0][i+2] and j<mat[1][i+1]: total += j+1
    for i,j in enumerate(mat[-1][1:-1]):# middle numbers of bot row
        if j<mat[-1][i] and j<mat[-1][i+2] and j<mat[-2][i+1]: total += j+1

    for i,row in enumerate(mat[1:-1]):
        # check first and last numbers
        if row[0]<row[1] and row[0]<mat[i][0] and row[0]<mat[i+2][0]:       total += row[0]+1   #first 
        if row[-1]<row[-2] and row[-1]<mat[i][-1] and row[-1]<mat[i+2][-1]: total += row[-1]+1  #last
        # check middle
        for j,k in enumerate(row[1:-1]):
            if k<row[j] and k<row[j+2] and k<mat[i][j+1] and k<mat[i+2][j+1]: total += k+1
    return total

def find_min(mat):
    coord_list = []
    # check corners
    if mat[0][0]<mat[0][1] and   mat[0][0]<mat[1][0]: coord_list.append((0,0))            #top left
    if mat[0][-1]<mat[0][-2] and mat[0][-1]<mat[1][-1]: coord_list.append((0,len(mat[0])-1))       #top right
    if mat[-1][0]<mat[-1][1] and mat[-1][0]<mat[-2][0]: coord_list.append((len(mat)-1,0))       #bot left
    if mat[-1][-1]<mat[-1][-2] and mat[-1][-1]<mat[-2][-1]: coord_list.append((len(mat)-1,len(mat[-1])-1))  #bot right
        
    for i,j in enumerate(mat[0][1:-1]): # middle numbers of top row
        if j<mat[0][i] and j<mat[0][i+2] and j<mat[1][i+1]: coord_list.append((0,i+1))

    for i,j in enumerate(mat[-1][1:-1]):# middle numbers of bot row
        if j<mat[-1][i] and j<mat[-1][i+2] and j<mat[-2][i+1]: coord_list.append((len(mat)-1,i+1))

    for i,row in enumerate(mat[1:-1]):
        # check first and last numbers
        if row[0]<row[1] and row[0]<mat[i][0] and row[0]<mat[i+2][0]:       coord_list.append((i+1,0))   #first 
        if row[-1]<row[-2] and row[-1]<mat[i][-1] and row[-1]<mat[i+2][-1]: coord_list.append((i+1,len(row)-1))  #last
        # check middle
        for j,k in enumerate(row[1:-1]):
            if k<row[j] and k<row[j+2] and k<mat[i][j+1] and k<mat[i+2][j+1]: coord_list.append((i+1,j+1))
    return coord_list
# test find_min(mat) so that the sum of all pulled coordinates is the same as solve2

def find_basin(mat,coord):
    length, width = mat.shape
    temp = coord # check which steps go wrong on min_coord[2]
    #print(min_coord)
    n = 1
    already = []
    #print('initial temp:',temp)
    while temp:
        #print(temp[0],mat[temp[0][0],temp[0][1]])
        # solve infinity loop when starting in the middle
        # maybe add "in already" rule after finding each
        if temp[0][0] == 0 and temp[0][1] == 0: # top left
            #print('found top left')
            if mat[0,0] < mat[0,1] and mat[0,1] != 9 and (0,1) not in already: # check adjacent
                n += 1
                temp.append((0,1))
                already.append((0,1))
            if mat[0,0] < mat[1,0] and mat[1,0] != 9 and (1,0) not in already: # check below
                n += 1
                temp.append((1,0))
                already.append((1,0))
        elif temp[0][0] == 0 and temp[0][1] == width-1: # top right
            #print('found top right')
            if mat[0,width-1] < mat[0,width-2] and mat[0,width-2] != 9 and (0,width-2) not in already: # check adjacent
                n += 1
                temp.append((0,width-2))
                already.append((0,width-2))
            if mat[0,width-1] < mat[1,width-1] and mat[1,width-1] != 9 and (1,width-1) not in already: # check below
                n += 1
                temp.append((1,width-1))
                already.append((1,width-1))
        elif temp[0][0] == length-1 and temp[0][1] == 0: # bottom left
            #print('found bottom left')
            if mat[length-1,0] < mat[length-1,1] and mat[lenght-1,1] != 9 and (length-1,1) not in already: # check adjacent
                n +=1
                temp.append((length-1,1))
                already.append((length-1,1))
            if mat[length-1,0] < mat[length-2,0] and mat[length-2,0] != 9 and (length-2,0) not in already: # check above
                n +=1
                temp.append((length-2,0))
                already.append((length-2,0))
        elif temp[0][0] == length-1 and temp[0][1] == width-1: # bottom right
            #print('found bottom right')
            if mat[length-1,width-1] < mat[length-1,width-2] and mat[length-1,width-2] != 9 and (length-1,width-2) not in already: # check adjacent
                n += 1
                temp.append((length-1,width-2))
                already.append((length-1,width-2))
            if mat[length-1,width-1] < mat[length-2,width-1] and mat[length-2,width-1] != 9 and (length-2,width-1) not in already: # check above
                n += 1
                temp.append((length-2,width-1))
                already.append((length-2,width-1))
        elif temp[0][0] == 0:  # top side
            #print('found top middle')
            if mat[0,temp[0][1]] < mat[0,temp[0][1]+1] and mat[0,temp[0][1]+1] != 9 and (0,temp[0][1]+1) not in already: # check adjacent right 
                n += 1
                temp.append((0,temp[0][1]+1))
                already.append((0,temp[0][1]+1))
            if mat[0,temp[0][1]] < mat[0,temp[0][1]-1] and mat[0,temp[0][1]-1] != 9 and (0,temp[0][1]-1) not in already: # check adjacent left
                n += 1
                temp.append((0,temp[0][1]-1))
                already.append((0,temp[0][1]-1))
            if mat[0,temp[0][1]] < mat[1,temp[0][1]] and mat[1,temp[0][1]] != 9 and (1,temp[0][1]) not in already: # check below
                n += 1
                temp.append((1,temp[0][1]))
                already.append((1,temp[0][1]))
        elif temp[0][0] == length - 1: # bottom side
            #print('found bottom middle')
            if mat[length-1,temp[0][1]] < mat[length-1,temp[0][1]+1] and mat[length-1,temp[0][1]+1] != 9 and (length-1,temp[0][1]+1) not in already: # check adjacent right 
                n += 1
                temp.append((length-1,temp[0][1]+1))
                already.append((length-1,temp[0][1]+1))
            if mat[length-1,temp[0][1]] < mat[length-1,temp[0][1]-1] and mat[length-1,temp[0][1]-1] != 9 and (0,temp[0][1]-1) not in already: # check adjacent left
                n += 1
                temp.append((length-1,temp[0][1]-1))
                already.append((length-1,temp[0][1]-1))
            if mat[length-1,temp[0][1]] < mat[length-2,temp[0][1]] and mat[length-2,temp[0][1]] != 9 and (length-2,temp[0][1]) not in already: # check above
                n += 1
                temp.append((length-2,temp[0][1]))
                already.append((length-2,temp[0][1]))
        elif temp[0][1] == 0: # left side
            #print('found side left')
            if mat[temp[0][0],0] < mat[temp[0][0],1] and mat[temp[0][0],1] != 9 and (temp[0][0],1) not in already: # check adjacent
                n += 1
                temp.append((temp[0][0],1))
                already.append((temp[0][0],1))
            if mat[temp[0][0],0] < mat[temp[0][0]-1,0] and mat[temp[0][0]-1,0] != 9 and (temp[0][0]+1,0) not in already: # check below
                n += 1
                temp.append((temp[0][0]+1,0))
                already.append((temp[0][0]+1,0))
            if mat[temp[0][0],0] < mat[temp[0][0]+1,0] and mat[temp[0][0]+1,0] != 9 and (temp[0][0]-1,0) not in already: # check above
                n += 1
                temp.append((temp[0][0]-1,0))
                already.append((temp[0][0]-1,0))
        elif temp[0][1] == width-1: # right side
            #print('found side right')
            if mat[temp[0][0],width-1] < mat[temp[0][0],width-2] and mat[temp[0][0],width-2] != 9 and (temp[0][0],width-2) not in already: # check adjacent
                n += 1
                temp.append((temp[0][0],width-2))
                already.append((temp[0][0],width-2))
            if mat[temp[0][0],width-1] < mat[temp[0][0]-1,width-1] and mat[temp[0][0]-1,width-1] != 9 and (temp[0][0]-1,width-1) not in already: # check below
                n += 1
                temp.append((temp[0][0]-1,width-1))
                already.append((temp[0][0]-1,width-1))
            if mat[temp[0][0],width-1] < mat[temp[0][0]+1,width-1] and mat[temp[0][0]+1,width-1] != 9 and (temp[0][0]+1,width-1) not in already: # check above
                n += 1
                temp.append((temp[0][0]+1,width-1))
                already.append((temp[0][0]+1,width-1))
        else: # everythin else
            #print('found something in the middle',temp[0],len(already))
            if mat[temp[0][0],temp[0][1]] < mat[temp[0][0],temp[0][1]+1] and mat[temp[0][0],temp[0][1]+1] != 9 and (temp[0][0],temp[0][1]+1) not in already: # check right
                n += 1
                temp.append((temp[0][0],temp[0][1]+1))
                already.append((temp[0][0],temp[0][1]+1))
            if mat[temp[0][0],temp[0][1]] < mat[temp[0][0],temp[0][1]-1] and mat[temp[0][0],temp[0][1]-1] != 9 and (temp[0][0],temp[0][1]-1) not in already: # check left
                n += 1
                temp.append((temp[0][0],temp[0][1]-1))
                already.append((temp[0][0],temp[0][1]-1))
            if mat[temp[0][0],temp[0][1]] < mat[temp[0][0]-1,temp[0][1]] and mat[temp[0][0]-1,temp[0][1]] != 9 and (temp[0][0]-1,temp[0][1]) not in already: # check below
                n += 1
                temp.append((temp[0][0]-1,temp[0][1]))
                already.append((temp[0][0]-1,temp[0][1]))
            if mat[temp[0][0],temp[0][1]] < mat[temp[0][0]+1,temp[0][1]] and mat[temp[0][0]+1,temp[0][1]] != 9 and (temp[0][0]+1,temp[0][1]) not in already: # check above
                n += 1
                temp.append((temp[0][0]+1,temp[0][1]))
                already.append((temp[0][0]+1,temp[0][1]))
        temp.pop(0)
    #print('already:',already,'length:',len(set(already))+1)
    return len(already) + 1

def solve2(mat,min_list):
    #print(mat)
    #print(min_list)
    basin_size = []
    for i in min_list:
        #print(len(basin_size))
        basin_size.append(find_basin(mat,[i]))
    basin_size.sort(reverse=True)
    print(basin_size[0]*basin_size[1]*basin_size[2]) 

test_inp = parse_input('test.txt')
# TODO: write a loop that goes through find_min(test_inp) checks if find_basin gives a higher value than min(result) and multiplies the results
min_list_test = find_min(test_inp)
solve2(test_inp,min_list_test)
#test = solve1(mat)
#assert test == 13, test
inp = parse_input('input.txt')
#print('input',solve1(inp))
min_list = find_min(inp)
#print(min_list)
solve2(inp,min_list)

