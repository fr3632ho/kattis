words = raw_input()
out = list(words)
n = len(words)
i = j = 0
while i<n:
    curr = words[i]
    if curr=='<' and j>=0:
        j=max(j-1,0)
        out[j]=' '
    else:
        out[j] = curr
        j+=1
    i+=1

if j>0:
    print "".join(out[:j])
