t=input()
for _ in range(t):
    n=input()
    nums = []
    for i in range(n):
        q = raw_input()
        nums.append((q.rjust(len(q)+1,'1').ljust(11,'0'), len(q)))
    nums.sort()
    out = "YES"
    for i in range(1,n):
        a1,l1 = nums[i-1]
        a2,_ = nums[i]
        if a1[1:l1+1]==a2[1:l1+1]:
            out = "NO"
            break
    print out
