n=int(input())
vals = list(map(int, input().split()))
if n==1:
    print(1,1)
    exit(0)
seqs = []
j=0
while j<n-1:
    k = j+1
    if vals[j]>=vals[k]:
        while k<n and vals[k-1]>=vals[k]:
            k+=1
        seqs.append((j+1,k))
        j=k-1
    j+=1
seqs2 = []
for a,b in seqs:
    if vals[a-1]!=vals[b-1]: # remove sequences with [... a a a a ..]
        seqs2.append((a,b))
if not seqs2:
    print(1,1)
    exit(0)
if len(seqs2)>1:
    print("Impossible")
else:
    lo,hi = seqs2[0][0]-1,seqs2[0][1]-1
    first, last = vals[lo],vals[hi]
    # need to check so that the first element is not greater that hi+1
    # and that the last element is greater than lo-1
    if hi<n-1 and first>vals[hi+1] or (lo>0 and last<vals[lo-1]):
        print("Impossible")
        exit(0)
    print(seqs2[0][0],seqs2[0][1])
