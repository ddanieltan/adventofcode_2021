#%%
from typing import List
from dataclasses import dataclass

# Credits: https://pastebin.com/BbQ6Cinz
#%% Constants
openings = '{([<'
closings = '})]>'
closing_brackets = {cl: op for op, cl in zip(openings, closings)}
opening_brackets = {op: cl for op, cl in zip(openings, closings)}
POINTS = {")":3,"]":57,"}":1197,">":25137}
AUTOCOMPLETE = {")":1,"]":2,"}":3,">":4}

# %%
@dataclass
class Line:
    input:str
    
    def get_corrupted_symbol(self) -> str:
        """
        Returns first corrupted symbol if present
        """
        stack = []
        for ch in self.input:
            if ch in openings:
                stack.append(ch)
            elif ch in closings:
                popped = stack.pop()
                if closing_brackets[ch] != popped:
                    return ch
        
        return None
    
    def get_all_incomplete_symbols(self) -> List[str]:
        """
        Returns all incomplete openings
        """
        stack = []
        for ch in self.input:
            if ch in openings:
                stack.append(ch)
            elif ch in closings:
                stack.pop()
        
        return stack
    
    def part2_score(self) -> int:
        """
        Get incomplete openings
        Reverse order
        Fill with correct closings
        Compute and return score
        """
        incompletes = self.get_all_incomplete_symbols()
        incompletes = incompletes[::-1]
        closings = [opening_brackets[i] for i in incompletes]
        score = 0
        for cl in closings:
            score *= 5
            score += AUTOCOMPLETE[cl]
        return score


    


# %% Testing
a = Line("{([(<{}[<>[]}>{[]{[(<()>")
# a.get_corrupted_symbol()
# a.is_corrupted()
# a.points()
# %%
b = Line("[({(<(())[]>[[{[]{<()<>>")
# b.get_corrupted_symbol()
# b.get_all_incomplete_symbols()
b.part2_score()

# %%
def parse(s:str) -> List[Line]:
    lines = s.split('\n')
    lines = [Line(l) for l in lines]
    return lines

eg = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

parse(eg)

#%% Test
lines = parse(eg)
for line in lines:
    print(line.get_corrupted_symbol())


# %%
with open("input.txt","r") as f:
    lines = f.read().split('\n')
    inp = [Line(l) for l in lines]


# %% Part 1
# Check if line is_corrupted
# Return sum of points
def part1(inp:List[Line]) -> int:
    points = 0
    for line in inp:
        incorrect = line.get_corrupted_symbol()
        if incorrect is not None:
            points += POINTS[incorrect]
    return points

#%%
part1(inp)
# %% Part 2
def part2(inp:List[Line]) -> int:
    """
    Check uncorrupted lines
    Compute scores
    Sort and return median score
    """
    scores = []
    for line in inp:
        incorrect = line.get_corrupted_symbol()
        if incorrect is not None:
            continue
        else:
            scores.append(line.part2_score())
    
    scores.sort()
    return scores[len(scores)//2]

part2(inp)
# %%
