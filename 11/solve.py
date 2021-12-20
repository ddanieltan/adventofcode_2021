#%%
from typing import List
from dataclasses import dataclass
# %%
@dataclass
class Octopus:
    x:int
    y:int
    energy:int

    def add_energy(self, e:int=1):
        """
        Increments energy counter
        Default by 1
        """
        self.energy = int(self.energy) + e
    
    def reset_energy(self):
        """
        Resets energy to 0
        """
        self.energy = 0

@dataclass
class Map:
    step:int
    state:List[List[Octopus]]
    flashes:int

    def get_neighbours(self, starting:Octopus) -> List[Octopus]:
        """
        Returns list of valid neighbouring octopuses
        to the starting Octopus
        """
        max_y = len(self.state)-1
        max_x = len(self.state[0])-1

        # (deltax, deltay)
        directions = [ 
            (-1,1), #NW
            (0,1,), #N
            (1,1), #NE
            (-1,0), #W
            (1,0), #E
            (-1,-1), #SW
            (0,-1), #S
            (1,-1), #SE
            ]
        
        neighbours = []
        for deltax, deltay in directions:
            new_x = starting.x + deltax
            new_y = starting.y + deltay
            if new_x >= 0 and new_x <= max_x:
                if new_y >= 0 and new_y <= max_y:
                    neighbours.append(self.state[new_y][new_x])
        
        return neighbours

    def update(self):
        """
        Update state by 1 step
        """
        # Octopuses that already flashed
        flashed = []
        # Octopuses that need to flash
        todo = []

        # Increase all Octopus energy by 1
        for x in range(len(self.state[0])):
            for y in range(len(self.state)):
                o = self.state[y][x]
                if o.energy == 9:
                    o.reset_energy()
                    self.flashes+=1
                    flashed.append(o)
                    todo.extend(self.get_neighbours(o))
                else:
                    o.add_energy()
        
        while todo:
            o2 = todo.pop(0)
            if o2 not in flashed:
                if o2.energy == 9:
                    o2.reset_energy()
                    self.flashes +=1
                    flashed.append(o2)
                    todo.extend(self.get_neighbours(o2))
                else:
                    o2.add_energy()

        # Increment step
        self.step += 1
    
    def print(self) -> str:
        """
        Prints out map/state
        """
        print(f'\nStep:{self.step}')
        for x in range(len(self.state[0])):
            line = []
            for y in range(len(self.state)):
                o = self.state[y][x]
                line.append(str(o.energy))
            print(" ".join(line))
            




# %%
def parse(s:str) -> Map:
    lines = s.split('\n')
    octs = []
    for x in range(len(lines[0])):
        xxx = []
        for y in range(len(lines)):
            o = Octopus(x,y,lines[y][x])
            xxx.append(o)
    
        octs.append(xxx)
    
    return Map(step=0,state=octs,flashes=0)

#%%
eg = """11111
19991
19191
19991
11111"""

e = parse(eg)
o = Octopus(x=3,y=3,energy=1)
e.get_neighbours(o)

o = Octopus(x=0,y=0, energy=1)
e.get_neighbours(o)
# %% Step 1
e.update()
e.state
# %% Step 2
e.update()
e.state

# %%
eg = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

m1 = parse(eg)

# %%
for _ in range(11):
    m1.update()
    m1.print()

print(m1.flashes)
#%%
for i in range(101):
    m1.update()
    if i%10==0:
        m1.print()

print(m1.flashes)

#%%
part1 = """4721224663
6875415276
2742448428
4878231556
5684643743
3553681866
4788183625
4255856532
1415818775
2326886125"""


# %%
m2 = parse(part1)
for _ in range(101):
    m2.update()

print(m2.flashes)


# Credits: https://www.reddit.com/r/adventofcode/comments/rds32p/2021_day_11_solutions/
#%%
def get_nbrs(r, c):
    nbrs = []
    for y, x in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        if r + y >= 0 and r + y <= 9 and c + x >= 0 and c + x <= 9:
            nbrs.append((r + y, c + x))
    return nbrs


data = [[int(j) for j in list(line)] for line in open("input.txt").read().strip().split("\n")]
step = 0
flashes = 0
pt1 = 0
pt2 = None
while True:
    flashed = []
    nbrs = []
    # increase energy levels of all
    for r in range(len(data)):
        for c in range(len(data[r])):
            # flash octopus
            if data[r][c] == 9:
                data[r][c] = 0
                flashes += 1
                flashed.append((r, c))
                nbrs.extend(get_nbrs(r, c))
            else:
                data[r][c] += 1
    # increase adjacent octopuses recursivly
    while nbrs:
        nbr_r, nbr_c = nbrs.pop(0)
        if (nbr_r, nbr_c) not in flashed:
            if data[nbr_r][nbr_c] == 9:
                data[nbr_r][nbr_c] = 0
                flashes += 1
                if (nbr_r, nbr_c) not in flashed:
                    flashed.append((nbr_r, nbr_c))
                nbrs.extend(get_nbrs(nbr_r, nbr_c))
            else:
                data[nbr_r][nbr_c] += 1
    # check for answers
    if step + 1 == 100:
        pt1 = int(flashes)
    if len(flashed) == 100:
        pt2 = step + 1
        break

    step += 1

print(f"Part 1: {pt1}") #1657
print(f"Part 2: {pt2}") #515
# %%

# %%
