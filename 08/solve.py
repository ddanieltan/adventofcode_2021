#%%
from typing import List, Tuple
from dataclasses import dataclass

def parse(s:str) -> List[Tuple]:
    """
    Parse multiline string and return a List of Tuples
    Each Tuple containing:
    - front : List[str]
    - back : List[str]
    """
    ret = []
    lines = s.split('\n')
    for line in lines:
        if line == "":
            continue
        else:
            front = line.split(' | ')[0].split()
            back = line.split(' | ')[1].split()
            ret.append((front,back))

    return ret 
#%%
def part1(inp:List[Tuple]) -> int:
    """
    Given list of Tuples
    Check only back inputs
    For digits 1,4,7,8 
    Return total count
    """
    num_segments = set([2,4,3,7])
    ret = 0

    for i in inp:
        front, back = i
        for code in back:
            if len(code) in num_segments:
                ret +=1

    return ret

# Credit: https://github.com/Farbfetzen/Advent_of_Code/blob/main/python/2021/day08.py
#%%
def solve_mappings(patterns:List[str]):
    """
    Given list of patterns
    For each pattern, place in candidates for each of the 10 digits
    Apply rules to prune candidates until single candidate for each digit
    Return dictionary mapping pattern to digit 
    """

    LENGTH_TO_DIGIT = {
        2: (1, ),
        3: (7, ),
        4: (4, ),
        5: (2, 3, 5),
        6: (0, 6, 9),
        7: (8, )
    }

    candidates = [[] for _ in range(10)]
    for pattern in patterns:
        for digit in LENGTH_TO_DIGIT[len(pattern)]:
            candidates[digit].append(pattern)


    # # 1 and 4 have unique numbers of segments.
    d1 = candidates[1][0]
    d4 = candidates[4][0]

    # # 2, 5, and 6 must not contain both segments of 1.
    for i in (2, 5, 6):
        candidates[i] = [c for c in candidates[i] if not set(d1).issubset(set(c))]

    # # The intersection of 5 and 4 must have length 3.
    candidates[5] = [c for c in candidates[5] if len(set(d4).intersection(set(c))) == 3]

    # # The intersection of 2 and 4 must have length 2.
    candidates[2] = [c for c in candidates[2] if len(set(d4).intersection(set(c))) == 2]

    # # The intersection of 9 and 4 must have length 4.
    candidates[9] = [c for c in candidates[9] if len(set(d4).intersection(set(c))) == 4]

    # # The intersection of 3 and 1 must have length 2.
    candidates[3] = [c for c in candidates[3] if len(set(d1).intersection(set(c))) == 2]

    # # The intersection of 0 and 1 must have length 2 and between 0 and 4 is must have length 3.
    candidates[0] = [c for c in candidates[0] if 
        len(set(d1).intersection(set(c))) == 2 and len(set(d4).intersection(set(c))) == 3]

    assert all(len(c) == 1 for c in candidates)
    return {"".join(sorted(c[0])): i for i, c in enumerate(candidates)}

def part2(inp:List[Tuple]) -> int:
    """
    For inputs (front, back),
    Solve mapping using front
    Apply mapping to decipher back
    Return sum of all deciphered back values
    """
    ret = 0
    for line in inp:
        front, back = line
        mappings = solve_mappings(front)
        deciphered = [mappings.get("".join(sorted(code))) for code in back]
        ret += (deciphered[0]*1000 + deciphered[1]*100 + deciphered[2]*10 + deciphered[3])
    
    return ret



#%%
eg = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

#%%
with open("input.txt","r") as f:
    inp = parse(f.read())

#%%
for line in parse(eg):
    front, back = line
    solve_mappings(front)
q
#%%
eg1 = ["be","cfbegad", "cbdgef", "fgaecd", "cgeb", "fdcge", "agebfd", "fecdb", "fabcd","edb"]
mappings = solve_mappings(eg1)
mappings
#%%
# print(part1(parse(eg)))
# print(part1(inp))

#%%
part2(parse(eg))
    

# %%
part2(inp)
# %%
