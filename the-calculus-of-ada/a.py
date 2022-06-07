
'''Read input with generator instead of input(), much faster'''
import sys
itr = (line for line in sys.stdin.read().split('\n')) # buffer
inp = lambda: next(itr) # next iter
def ni(): return int(inp())
def nl(): return [int(tok) for tok in inp().split()]

def find_diff(numbers):
    diffs = []
    for i in range(len(numbers)-1):
        diffs.append(numbers[i+1] - numbers[i])     
    return diffs, len(set(diffs)) == 1


n, *vals = nl()
done = False
all_diffs = [vals]
while not done:
    diff, done = find_diff(all_diffs[-1])    
    all_diffs.append(diff)

for j in range(len(all_diffs)-1, 0, -1):
    all_diffs[j-1].append(all_diffs[j-1][-1] + all_diffs[j][-1])

print(len(all_diffs)-1, all_diffs[0][-1])

