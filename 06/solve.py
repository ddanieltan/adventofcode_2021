#%% 
from typing import List, Dict
from dataclasses import dataclass

# %%
@dataclass
class Group:
    day : int
    state : List[int]

    def count(self) -> int:
        """
        Returns number of fish in state
        """
        return len(self.state)
    
    def next_day(self):
        """
        - Increments day counter +1
        - For each fish in state, decrement -1
            - If fish prior was 0 reset to 6 and add a new fish
        """
        self.day += 1
        new_fish = 0
        tmp = []
        for fish in self.state[:]:
            if fish == 0:
                tmp.append(6)
                new_fish+=1
            else:
                tmp.append(fish-1)
        self.state = tmp + new_fish*[8]

# %%
def parse(s:str) -> List[int]:
    ret = s.split(',')
    ret = [int(r) for r in ret]
    return ret
# %%
eg ="3,4,3,1,2"
# %%
parse(eg)
#%%
g1 = Group(0,parse(eg))
for _ in range(80):
    g1.next_day()
g1.count()
# %% Part 1
with open("input.txt","r") as f:
    inp = f.read()
g1 = Group(0,parse(inp))
for _ in range(80):
    g1.next_day()
g1.count()

# %% Part 2
# Credits to: https://www.reddit.com/r/adventofcode/comments/r9z49j/2021_day_6_solutions/

@dataclass
class Counter:
    day: int
    counter: Dict

    def count(self):
        ret =0
        for _, v in self.counter.items():
            ret+=v
        return ret

    def next_day(self):
        self.day += 1
        tmp = self.counter[0]
        for i in range(1,9):
            self.counter[i-1] = self.counter[i]
        self.counter[8] = tmp
        self.counter[6] += tmp


#%%
def parse(s:str) -> Dict:
    """
    Parse inputs into a dictionary where
    - key: number of days left
    - value: number of fish
    """
    dd = dict().fromkeys([i for i in range(9)],0)
    for ss in s.split(','):
        num = int(ss)
        dd[num] += 1
    return dd
#%%
c1 = Counter(0,parse(eg))
c1
#%%
for _ in range(80):
    c1.next_day()
c1.count()
#%%
with open("input.txt","r") as f:
    inp = f.read()
dd = parse(inp)


#%%
c2 = Counter(0,parse(inp))
for _ in range(256):
    c2.next_day()
c2.count()
# %%
