#%%
from typing import List

#%%
def parse(input:str) -> List[int]:
    # Parse string as list
    list_ = input.split('\n')
    list_ = [int(l) for l in list_]
    return list_


#%%
def part1(inp:List[int]) -> int:
    """
    Given input as list of ints
    Return number of measurements larger than previous
    """
    
    # Shift list by 1 element
    a = inp[:-1]
    b = inp[1:]

    # Compare elements from a and b, retain only when b>a
    result = [i for i,j in zip(a,b) if i<j]
    return len(result)

#%%
example = """199
200
208
210
200
207
240
269
260
263"""
# %%
part1(parse(example))
# %%
with open("input.txt","r") as f:
    inp = f.read()
# %%
part1(parse(inp))
# %%
def part2(inp:List[int]) -> int:
    """
    Given input as multiline string
    Return number of times the sum of sliding window of 3 measurements increments
    """
    # Shift list by 1 element 3 times
    a = inp[:-2]
    b = inp[1:-1]
    c = inp[2:]

    # Sum elements of common index
    sums = [a[i]+b[i]+c[i] for i in range(len(a))]

    return part1(sums)
# %%
part2(parse(example))
# %%
part2(parse(inp))
# %%
