import random
import matrix_transpose




column_sep=['|', '|', '|', '']
line_sep=['-', '-', '-', '']
num_choices=[4]+[2]*9
cell_width=5


def print_board(gb):
    for r in range(4):
        for c in range(4):
            print(str(gb[r][c]).center(cell_width) if gb[r][c] else " "*cell_width, end=column_sep[c])
        print("\n" + line_sep[r]*23)

def place_new_value(gb):
    # This function places a 2 or 4 into an empty cell in gb
    pass

def game_over(gb):
    # This function returns True if the game is over and False otherwise
    print("Check game over")

def shift_cells(cell_list):
    # always shift cell_list to the left (towards 0 index)
    # there are 4 elements, may have element with 0 value (
    # empty cells)  
    # 1. remove the 0 value cells (clear the spaces)
    # 2. shift cell_list to the left
    #       i. if len(cell_list)>1 then start with the 0 element and
    #           check if neighbors are the same and combine
    #       ii. move on to the next elements to check for neighbors
    #           to combine.  At most, there are only two combinations
    # 3. add in the correct number of 0 (empty spaces) to the right
    #   to make the final length = 4
    # returns True/False if cells shifted 
    orig_list=cell_list.copy()
    while 0 in cell_list:
        cell_list.remove(0)

    i=0
    while i+1<len(cell_list):
        if cell_list[i]==cell_list[i+1]:
           cell_list[i]*=2
           cell_list.pop(i+1)
        i+=1
            
    cell_list+=[0]*(4-len(cell_list))
    return not orig_list==cell_list

# directions are: 0: up, 1: right, 2: down, 3: left
def play(gb, direction):
    print("Direction: ", direction)

    shifted=False
    if direction=='left':
        for row in range(4):
            shifted = True if shift_cells(gb[row]) else shifted
    elif direction=='right':
        for row in range(4):
            gb[row].reverse()
            shifted = True if shift_cells(gb[row]) else shifted
            gb[row].reverse()
    else:
        # transpose
      pass   
            
        
    
# test cases for game_over
# make sure your code can pass these test cases

gb=[[0,2,4,8],
    [2,4,8,2],
    [4,8,2,4],
    [8,2,4,2]]
print("Should be false: ", game_over(gb))

gb=[[4,2,4,8],
    [2,0,8,2],
    [4,8,2,4],
    [8,2,4,2]]
print("Should be false: ", game_over(gb))

gb=[[4,2,4,8],
    [2,4,8,2],
    [4,8,0,4],
    [8,2,4,2]]
print("Should be false: ", game_over(gb))

gb=[[4,2,4,8],
    [2,4,8,2],
    [4,8,2,4],
    [8,2,4,0]]
print("Should be false: ", game_over(gb))

gb=[[0,2,4,8],
    [2,4,8,2],
    [4,8,2,4],
    [8,2,4,0]]
print("Should be false: ", game_over(gb))

gb=[[0,2,4,8],
    [2,4,0,2],
    [4,8,2,4],
    [8,2,4,0]]
print("Should be false: ", game_over(gb))

gb=[[0,2,4,8],
    [2,4,0,2],
    [4,0,2,4],
    [8,2,4,0]]
print("Should be false: ", game_over(gb))


gb=[[4,2,4,8],
    [2,4,8,2],
    [4,8,2,4],
    [8,2,4,2]]
print("Should be true: ", game_over(gb))

gb=[[8,2,4,8],
    [2,4,16,2],
    [4,32,2,4],
    [8,2,4,64]]
print("Should be true: ", game_over(gb))

gb=[[4,2,2,8],
    [2,4,8,2],
    [4,8,2,4],
    [8,2,4,2]]
print("Should be false: ", game_over(gb))

gb=[[4,2,8,8],
    [2,4,8,2],
    [4,8,2,4],
    [8,2,4,2]]
print("Should be false: ", game_over(gb))

    
# test cases for shift_cells
# make sure your code can pass these test cases

sl=[0]*4
shift_cells(sl)

sl=[2,0,0,0]
shift_cells(sl)

sl=[0,2,0,0]
shift_cells(sl)

sl=[0,0,0,2]
shift_cells(sl)

sl=[0,2,0,4]
shift_cells(sl)

sl=[0,2,4,8]
shift_cells(sl)

sl=[2,2,0,0]
shift_cells(sl)

sl=[2,0,2,0]
shift_cells(sl)

sl=[2,0,0,2]
shift_cells(sl)

sl=[2,2,0,2]
shift_cells(sl)

sl=[2,0,2,2]
shift_cells(sl)

sl=[2,2,2,2]
shift_cells(sl)

sl=[4,2,4,2]
shift_cells(sl)

sl=[0,2,2,0]
shift_cells(sl)

sl=[0,2,2,4]
shift_cells(sl)

sl=[8,4,2,2]
shift_cells(sl)

sl=[2,2,8,4]
shift_cells(sl)

sl=[8,4,0,4]
shift_cells(sl)

sl=[2,16,4,4]
shift_cells(sl)

sl=[4,16,4,4]
shift_cells(sl)

sl=[2,2,16,8]
shift_cells(sl)

sl=[2,4,16,16]
shift_cells(sl)

sl=[2,2,0,32]
shift_cells(sl)

sl=[2,2,4,32]
shift_cells(sl)

sl=[0,8,8,2]
shift_cells(sl)

sl=[2,8,8,0]
shift_cells(sl)

sl=[2,0,8,8]
shift_cells(sl)
