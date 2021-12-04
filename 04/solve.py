#%%
from typing import List, Tuple
from dataclasses import dataclass

# %%
@dataclass
class Board:
    numbers: List[List[int]]
    hits: List[List[int]]

    def is_won(self)->bool:
        """
        Checks each row and col of hits matrix
        Returns true if sum to 5 otherwise false
        """
        for row in self.hits:
            if sum(row) == 5:
                return True
        
        for i in range(5):
            column = [row[i] for row in self.hits]
            if sum(column) == 5:
                return True
        
        return False
    
    def update(self, comp:int):
        """
        Given a comparison (comp), update hits matrix if matching numbers matrix
        """
        for row in range(5):
            for col in range(5):
                if self.numbers[row][col] == comp:
                    self.hits[row][col] = 1
    
    def get_unmarked_sum(self) -> int:
        """
        Returns sum of all unmarked numbers
        """
        ret = 0
        for row in range(5):
            for col in range(5):
                if self.hits[row][col] == 0:
                    ret += self.numbers[row][col]
        
        return ret




# %%
numbers = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
hits = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
b1 = Board(numbers, hits)
# %%
b1.is_won()
# %%
b1.update(21)
# %%
b1.hits
# %%
b1.get_unmarked_sum()
# %%
eg ="""7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""
# %%
def parse(s:str) -> Tuple:
    """
    Input: Multi line string
    Output: Tuple
        1. List of each Bingo number
        2. List of Boards
    """

    sections = s.split('\n')
    a = sections[0]
    b = sections[1:]

    # Bingo instructions
    bingo = a.split(",")
    bingo = [int(b) for b in bingo]

    # List of Boards
    boardlines = []
    for line in b:
        if line == "":
            continue
        else:
            numline = line.split()
            numline = [int(n) for n in numline]
            boardlines.append(numline)
    
    assert len(boardlines)%5 == 0
    num_boards = int(len(boardlines)/5)
    
    boards = []
    for f in range(num_boards):
        board_array = []
        for g in range(5):
            #index
            i = g + f*5
            board_array.append(boardlines[i])
        
        hits = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        bb = Board(board_array, hits)
        boards.append(bb)

    return bingo,boards
# %%
bingo, boards = parse(eg)

# %%
def part1(bingo, boards) -> int:
    """
    Iterate through each number(comp) in bingo instructions
    If boards have a winner, return unmarked numbers * winning comp
    Else, update boards with comp
    """

    for comp in bingo:
        print(f'comp:{comp}')
        for board in boards:
            print(f'Board_before_hits:{board.hits}')
            board.update(comp)
            print(f'Board_after_hits:{board.hits}')
            if board.is_won():
                print('Won!')
                print(f'unmarkedsum:{board.get_unmarked_sum()}')
                print(f'comp:{comp}')
                return board.get_unmarked_sum() * comp

    return -1
# %%
part1(bingo,boards)
# %%
with open("input.txt","r") as f:
    bingo,boards = parse(f.read())
# %%
part1(bingo,boards)
# %%
def part2(bingo,boards) -> int:
    """
    Update boards with bingo instructions
    Prune away boards that have won until last board left
    Return unmarked numbers * winning comp
    """

    candidates = boards.copy()

    for comp in bingo:
        print(f'comp:{comp}')

        if len(candidates)==1:
            bb = candidates[0]
            bb.update(comp)
            if bb.is_won():
                return bb.get_unmarked_sum() * comp
        else:

            for board in candidates[:]:
                board.update(comp)
                if board.is_won():
                    candidates.remove(board)

                
    
    return -1
                
            
            
# %%
bingo, boards = parse(eg)
# %%
part2(bingo,boards)
# %%
with open("input.txt","r") as f:
    bingo,boards = parse(f.read())
part2(bingo,boards)
# %%
