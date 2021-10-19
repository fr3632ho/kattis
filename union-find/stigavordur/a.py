
def gcd(a, b):
    if a < b: return gcd(b,a)
    if b==0: return a
    return gcd(b, a%b)

n, q = map(int, input().split())
nums = list(map(int, input().split()))
print(n,q)
print(nums)

# array1 -> nums
# array2 -> min gcd of chunk
# chunk -> #sqrt(n) elements
#
