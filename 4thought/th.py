import sys

op = ['-', '+', '*', '//']
nums = dict()
for i in op:
    for j in op:
        for h in op:
            out = "4 {:s} 4 {:s} 4 {:} 4".format(i,j,h)
            val = eval(out)
            nums[val] = out.replace("//","/")


m = int(input())
for _ in range(m):
    n = int(input())
    if not -60 <= n <= 4**4:
        print("no solution")
        continue

    if n in nums:
        print(nums[n] + " = " + str(n))
        continue
    print("no solution")
