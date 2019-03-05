

def shift_cells(cell_list):
    # always shift cell_list to the left (towards 0 index)
    # there are 4 elements, may have element(s) with 0 value (
    # empty cells)
    print("Initial list: ", cell_list)

# directions are: 0: up, 1: right, 2: down, 3: left
def play(gb, direction):
    print("Direction: ", direction)
    
# test cases
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
