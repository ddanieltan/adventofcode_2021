#%%
from typing import List

# %%
def parse(s:str) -> List[str]:
    """
    Input: Multiline string
    Output: List of strings
    """
    ret = s.split('\n')
    return ret
# %%
eg = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""
# %%
parse(eg)
# %%
def part1(inp:List[str]) -> int:
    """
    Keep track of horizontal and depth
    Update per inputs
    Return product of horizontal and depth
    """
    x = 0 #horizontal
    y = 0 #depth
    for i in inp:
        command = i.split()[0]
        value = int(i.split()[1])
        if command == "forward":
            x+=value
        if command == "up":
            y-=value
        if command == "down":
            y+=value
    
    return x*y

# %%
part1(parse(eg))
# %% puzzle input
with open("input.txt","r") as f:
    inp = f.read()

# %%
part1(parse(inp))
# %%
def part2(inp:List[str])->int:
    """
    Keep track of horizontal, depth and aim
    Update per inputs
    Return product of horizontal and depth
    """
    x=0
    y=0
    aim=0
    for i in inp:
        command = i.split()[0]
        value = int(i.split()[1])
        if command == "forward":
            x+=value
            y += aim * value
        if command == "up":
            aim-=value
        if command == "down":
            aim+=value
    return x*y
# %%
part2(parse(eg))
# %%
part2(parse(inp))
# %%
