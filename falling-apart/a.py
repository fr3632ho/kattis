n = input()
nums = list(map(int,raw_input().split()))
nums.sort(key=lambda x : -x)
a = b = 0
for i in range(n):
    a += (i%2==0)*nums[i]
    b += (i%2!=0)*nums[i]
print a, b
