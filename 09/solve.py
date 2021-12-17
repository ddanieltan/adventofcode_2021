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

@dataclass
class Map:
    map : List[List[Point]]

    def low_points(self) -> int:
        """
        Find the dimensions of the map
        Iterate through every Point and compare against adjacent Points
        Return low points
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
        
        return low_points
    
    def get_basin_points(self, starting:Point) -> List[Point]:
        """
        Given a starting Point, return list of Points of all
        adjacent Points not 9
        """
        explored = []
        moves = 
    
    def largest_basins(self) -> int:
        """
        Start with list of lowest Points
        For each point, log explored, compare if adjacent point is 9
        If not, add to Points to frontier
        Stop when no more points to explore

        Collect list of basins with sizes
        Return product of top 3 largest basins
        """

        lowest_points = self.low_points()
        frontier = [] # List of Points to explore
        explored = [] # List of Points already explored
        all_basins = []
        current_basin = []
       
        for point in lowest_points:
            if point in explored:
                continue
            else:
            
            
            if point.h < 9:
                current_basin.append(point)
                explored.append(point)


        return


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
9856789892
8767896789
9899965678"""

m = parse(eg)
m.low_points()

#%% 
with open("input.txt","r") as f:
    m = parse(f.read())

# %% Part 1
low_points = m.low_points()
ret = 0
for point in low_points:
    ret += (point.h + 1)
print(ret)

# %%
