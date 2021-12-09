#%%
from typing import List, Dict
from dataclasses import dataclass

@dataclass
class Positions():
    starting:Dict
    
    def calculate_cost(self, position):
        """
        Given a position to shift each crab to
        Return the total cost of moving
        """
        cost = 0
        for starting, num in self.starting.items():
            if starting == position:
                continue
            if starting < position:
                cost += (position-starting)*num
            if starting > position:
                cost += (starting-position)*num
        
        return cost
    
    def iterate(self) -> int:
        """
        Iterate through all the position positions to shift to
        Return the lowest cost
        """
        min_cost = 1_000_000
        for i in range(max(self.starting.keys())+1):
            cost = self.calculate_cost(i)
            if cost < min_cost:
                min_cost = cost
        
        return min_cost






#%%
def parse(s:str) -> Dict:
    ll = s.split(',')
    ll = [int(l) for l in ll]
    ret = dict()
    for i in ll:
        ret[i] = ret.get(i,0) + 1
    return ret
# %%
eg="16,1,2,0,4,2,7,1,2,14"
parse(eg)
# %%
p1 = Positions(parse(eg))
p1.iterate()
# %%
with open("input.txt","r") as f:
    inp = parse(f.read())
# %% Part 1
p1 = Positions(inp)
p1.iterate()
# %% Part 2
@dataclass
class Positions():
    starting:Dict
    
    def calculate_cost(self, position):
        """
        Given a position to shift each crab to
        Return the total cost of moving
        """
        cost = 0
        for starting, num in self.starting.items():
            if starting == position:
                continue
            if starting < position:
                delta = (position-starting)
                steps = (delta * (delta+1))/2
                cost += steps*num
            if starting > position:
                delta = (starting-position)
                steps = (delta * (delta+1))/2
                cost += steps*num
        
        return cost
    
    def iterate(self) -> int:
        """
        Iterate through all the position positions to shift to
        Return the lowest cost
        """
        min_cost = 1_000_000_000
        for i in range(max(self.starting.keys())+1):
            cost = self.calculate_cost(i)
            if cost < min_cost:
                min_cost = cost
        
        return int(min_cost)

# %%
p2 = Positions(parse(eg))
p2.iterate()
# %%
p2 = Positions(inp)
p2.iterate()
# %%
