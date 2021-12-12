#%%
import dataclasses
from typing import List, Tuple
from dataclasses import dataclass
# %%
@dataclass
class Point:
    x : int
    y : int
    h : int # height

    def get_adjacent_xy(self) -> List[Tuple[int,int]]:
        """
        Returns List of (x,y) valid adjacent points
        """
        ret = []

        

@dataclass
class Map:
    map : List[List[Point]]

    def search(self) -> int:
        """
        Find the dimensions of the map
        Iterate through every Point and compare against adjacent Points
        Record low Points
        Return sum of (low points +1)
        """
        max_y = len(self.map)-1
        max_x = len(self.map[0])-1
        low_points = []

        for x in range(max_x+1):
            for y in range(max_y+1):
                
                p = self.map[y][x]
                # Get valid adjacent Points
                comparisons = []
                if (y - 1 >= 0): # Up (-1, 0)
                    comparisons.append(self.map[y-1][x])
                if (y + 1 <= max_y): # Down (1, 0)
                    comparisons.append(self.map[y+1][x])
                if (x-1 >= 0): # Left (0, -1)
                    comparisons.append(self.map[y][x-1])
                if (x+1 <= max_x): # Right (0, 1)
                    comparisons.append(self.map[y][x+1])
                
                if all(p.h < adj.h for adj in comparisons):
                    low_points.append(p)
        
        ret = 0
        for point in low_points:
            ret += (point.h + 1)
        return ret



#%%
def parse(s:str) -> Map:
    """
    Parse multiline string into Map
    """
    lines = s.split('\n')

    map_list = []
    for y, line in enumerate(lines):
        line_list = []
        for x, val in enumerate(line):
            p = Point(x=x,y=y,h=int(val))
            line_list.append(p)
        map_list.append(line_list)
    
    m = Map(map_list)

    return m
            
            
eg = """2199943210
3987894921
9856789892q
8767896789
9899965678"""

m = parse(eg)
m.search()



#%% 
with open("input.txt","r") as f:
    m = parse(f.read())

# %% Part 1
m.search()

# %%
