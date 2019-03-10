def game_over(gb):
    # This function returns True if the game is over and False otherwise
    print("Check game over")

def shift_cells(cell_list):
    # always shift cell_list to the left (towards 0 index)
    # there are 4 elements, may have element(s) with 0 value (
    # empty cells)
    print("Initial list: ", cell_list)

# directions are: 0: up, 1: right, 2: down, 3: left
def play(gb, direction):
    print("Direction: ", direction)
    
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
