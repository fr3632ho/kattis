n,q=map(int,raw_input().split())
dp=[0]
values=list(map(int,raw_input().split()))
dp.extend(values)
for i in range(100*110):
    best=dp[-1]+values[0]
    for j in range(1,n+1):
        energy = values[j-1]
        best=min(best, energy+dp[-j])
    dp.append(best)
besti=0 # find the best release of energy for nr. of neutrons per unit of energy
        # released
for i in range(1,n):
    if values[i]/(i+1.0) < values[besti]/(besti+1.0):
        besti=i
for query in range(q):
    k= input()
    tot=0
    if k>= len(dp):
        diff = k-len(dp)
        subs=diff//(besti+1) + 1
        tot = subs*values[besti]
        k=k-subs*(besti+1)
    tot+= dp[k]
    print tot
