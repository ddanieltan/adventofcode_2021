#%%
import re
from typing import List, Tuple
from dataclasses import dataclass

@dataclass
class Line:
    x1: int
    y1: int
    x2: int
    y2: int

    def is_not_diagonal(self) -> bool:
        """
        Returns true if coordinates don't make a diagonal line, else false
        """
        if (self.x1 == self.x2) or (self.y1==self.y2):
            return True
        return False
    
    def get_coordinates(self) -> List[Tuple[int]]:
        """
        Assume line is horizontal or vertical
        Returns all the coordinates as a list of tuples
        """
        ret = []

        # Horizontal line
        if self.x1 == self.x2:
            x = self.x1
            if self.y1 < self.y2:
                for y in range(self.y1,self.y2+1):
                    ret.append((x,y))
            else:
                for y in range(self.y2, self.y1+1):
                    ret.append((x,y))
        
        # Vertical line
        elif self.y1 == self.y2:
            y = self.y1
            if self.x1 < self.x2:
                for x in range(self.x1, self.x2+1):
                    ret.append((x,y))
            else:
                for x in range(self.x2, self.x1+1):
                    ret.append((x,y))
        

        # Diagonal line (part2)
        else:
            delta_x = 1
            delta_y = 1

            if self.x1 > self.x2:
                delta_x = -1
            if self.y1 > self.y2:
                delta_y = -1
            
            currx = self.x1
            curry = self.y1

            if delta_x == 1:
                for x in range(self.x1, self.x2 + 1, delta_x):
                    ret.append((currx,curry))
                    currx += delta_x
                    curry += delta_y
            if delta_x == -1:
                for x in range(self.x1+1, self.x2, delta_x):
                    ret.append((currx,curry))
                    currx += delta_x
                    curry += delta_y
        
        return ret

#%%
@dataclass
class Map:
    lines : List[Line]
    mmap = None

    def __init__(self, lines:List[Line]):
        # Finding how large map needs to be
        max_x = 0
        max_y = 0
        self.lines = lines
        for line in self.lines:
            if line.x1 > max_x:
                max_x = line.x1
            if line.x2 > max_x:
                max_x = line.x2
            if line.y1 > max_y:
                max_y = line.y1
            if line.y2 > max_y:
                max_y = line.y2

        self.mmap = []
        row = [0] * (max_x+1)
        for i in range(max_y+1):
            self.mmap.append(row)
    
    def update_map(self, x:int, y:int):
        """
        Given coordinate of map (x,y) add 1 to value in map cell
        """
        matrix = []
        for i,m in enumerate(self.mmap[:]):
            if i == y:
                tmp = m.copy()
                tmp[x] +=1
                matrix.append(tmp)
            else:
                matrix.append(m)
        
        self.mmap = matrix

    def draw_map(self):
        """
        Draw map from current lines
        - Check if line is not diagonal
        - Cells on map for non diagonal lines +1
        - Print out points where value >=2
        """

        # Check if line is not diagonal and update
        for line in self.lines:
            # part 2
            #if line.is_not_diagonal():
            coordinates = line.get_coordinates()
            for x,y in coordinates:
                self.update_map(x,y)
        
        # Print out the map
        # Print out number of cells >2

        counter=0
        for row in self.mmap:
            print(row)
            for cell in row:
                if cell >=2:
                    counter+=1
        
        print(f'Counter:{counter}')
        

#%%
def parse(s:str) -> List[Line]:
    """
    Input: Multiline string
    Output: List of Lines
    """
    ret = []
    inputs = s.split("\n")
    for i in inputs:
        search_pattern = r"(\d+),(\d+) -> (\d+),(\d+)"
        regex = re.search(search_pattern, i)
        l = Line(
            x1 = int(regex[1]),
            y1 = int(regex[2]),
            x2 = int(regex[3]),
            y2 = int(regex[4])
        )
        ret.append(l)
    
    return ret

# %%
eg = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""
# %%
parse(eg)
# %%
m = Map(parse(eg))
# %%
m.draw_map()

#%% Part 1
with open("input.txt","r") as f:
    inp = parse(f.read())

# %%
m1 = Map(inp)
# %%
m1.draw_map()
# %% Testing diagonal line
l = Line(x1=8, y1=0, x2=0, y2=8)
l.get_coordinates()
# %% Part 2
m2 = Map(inp)
m2.draw_map()

# %%
