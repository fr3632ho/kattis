d = {'R':'S','B':'K','L':'H'}
s = raw_input()
out = []
for i in range(len(s)):
    out.append(d[s[i]])
    q = out[-3:]
    q.sort()
    if q == ['H','K','S']:
        for i in range(3):
            out.pop()
        out.append('C')
print "".join(out)
