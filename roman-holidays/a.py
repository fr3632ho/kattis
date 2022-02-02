numerals = [(1, 'I'), (2, 'II'), (3, 'III'), (4, 'IV'), (5, 'V'), (6, 'VI'), (7, 'VII'), \
    (8, 'VIII'), (9, 'IX'), (10, 'X'), (20,'XX'), (30, 'XXX'), (40, 'XL'), (50, 'L'), (60, 'LX'), \
    (70, 'LXX'), (80, 'LXXX'), (90, 'XC'), (100, 'C'), (200, 'CC'), (300, 'CCC'), (400, 'CD'), \
    (500, 'D'), (600, 'DC'), (700, 'DCC'), (800, 'DCCC'), (900, 'CM'), (1000, 'M')]

def int_to_roman(i):
    # assume the number i is <= 1000
    out = []        
    while i > 1000:
        out.append('M')
        i -= 1000
    for val, r in reversed(numerals):
        if i-val >= 0:
            i-=val
            out.append(r)
            if i==0:
                break
    return ''.join(out)                

all_1000 = [(i, int_to_roman(i)) for i in range(1, 1001)]
neg =  [(i, r) for i, r in all_1000 if r.startswith('X') or r.startswith('V')]
pos = [ (i, r) for i, r in all_1000 if not (r.startswith('X') or r.startswith('V'))]

neg.sort(key=lambda x : x[1])
pos.sort(key=lambda x : x[1])
m_pos, m_neg = len(pos), len(neg)

from collections import defaultdict

indx_dict = defaultdict(int)
for idx, (_, r) in enumerate(pos):
    indx_dict[r] = idx+1

for idx, (_, r) in enumerate(reversed(neg)):
    indx_dict[r] = -(idx + 1)

n = int(input())
for _ in range(n):
    i = int(input())    
    out = 0
    if i == 1000:
        out = indx_dict['M']
    else:        
        r = i%1000                
        q = i//1000
        if r == 0:
            out = indx_dict['M'] * q
        else:            
            num = int_to_roman(r)
            r_num = indx_dict[num]                                    
            if r_num < 0:
                out = r_num + (-m_neg * q)
            else:
                out = r_num + (m_pos * q)

    print(out)

