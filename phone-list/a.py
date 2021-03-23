t=input()
for _ in range(t):
    n=input()
    nums = []
    for i in range(n):
        q = raw_input()
        nums.append((q.ljust(10,'0'), len(q)))
    nums.sort()
    print nums
    out = "YES"
    for i in range(1,n):
        a1,l1 = nums[i-1]
        a2,_ = nums[i]
        if a1[:l1]==a2[:l1]:
            out = "NO"
            break
    print out
