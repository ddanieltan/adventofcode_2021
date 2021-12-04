#%%
from typing import List

def parse(s:str)->List[str]:
    """
    Input: Multiline string
    Output: List of Strings, each string being a number eg. "00100"
    """
    inp = s.split('\n')
    return inp
# %%
eg = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""
# %%
parse(eg)
# %%
def part1(inp:List[str])->int:
    """
    Input: List of strings
    Output: Product of gamma and epsilon
    """
    gamma = ""
    epsilon = ""
    # Cycle through each index position
    for i in range(len(inp[0])):
        
        # Count occurances of zero and ones
        zero_counter = 0
        one_counter = 0

        for seq in inp:
            if seq[i] == "0":
                zero_counter+=1
            if seq[i] == "1":
                one_counter+=1
        
        # Most common bit is appended to gamma
        # Lease common bit is appended to epsilon
        if zero_counter > one_counter:
            gamma+="0"
            epsilon+="1"
        else:
            gamma+="1"
            epsilon+="0"
    
    # Convert binary to decimal
    G = int(gamma,2)
    E = int(epsilon,2)

    return G*E



# %%
part1(parse(eg))
# %%
with open("input.txt","r") as f:
    inp = parse(f.read())
# %%
part1(inp)

#%%
def most_common(bits:List[str]) -> str:
    """
    Input: List of bits, either "0" or "1"
    Returns the most common occuring bit, in a tie return "1"
    """
    zeroes = 0
    ones = 0
    for b in bits:
        if b == "0":
            zeroes +=1
        else:
            ones +=1
    if zeroes == ones:
        return "1"
    elif zeroes > ones:
        return "0"
    else:
        return "1"

def least_common(bits:List[str]) -> str:
    """
    Input: List of bits, either "0" or "1"
    Returns the least common occuring bit, in a tie return "0"
    """
    zeroes = 0
    ones = 0
    for b in bits:
        if b == "0":
            zeroes +=1
        else:
            ones +=1
    if zeroes == ones:
        return "0"
    elif zeroes > ones:
        return "1"
    else:
        return "0"

# %%

def part2(inp:List[str])->int:
    """
    Input: List of strings
    Output: Product of o2 and co2 ratings
    """

    o2_candidates = inp.copy()

    for i in range(len(inp[0])):
        if len(o2_candidates) == 1:
            break

        bits_at_i = []
        for seq in o2_candidates[:]:
            bits_at_i.append(seq[i])
        most_common_bit = most_common(bits_at_i)
        for seq in o2_candidates[:]:
            if seq[i] != most_common_bit:
                o2_candidates.remove(seq)
    
    o2 = int(o2_candidates[0],2)

    co2_candidates = inp.copy()

    for i in range(len(inp[0])):
        if len(co2_candidates) == 1:
            break
        bits_at_i = []
        for seq in co2_candidates[:]:
            bits_at_i.append(seq[i])
        least_common_bit = least_common(bits_at_i)
        for seq in co2_candidates[:]:
            if seq[i] != least_common_bit:
                co2_candidates.remove(seq)
    
    o2 = int(o2_candidates[0],2)
    co2 = int(co2_candidates[0],2)
    
    return o2 * co2


#%% Verifying default max() and min()
# Follows unique tiebreak rules
max(["1","1","0","0"])
# %%
part2(parse(eg))

# %% Use a slice if we want to iterate a list and mutate it at the same time
# Go through list, check condition and prune list 
x = [1,1,0,1,0,1,0]

for i in x[:]:
    print(x)
    if i == 1:
        x.remove(i)

# %%
part2(inp)
# %%
