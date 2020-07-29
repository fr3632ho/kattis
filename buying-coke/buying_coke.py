import sys

'''
Dynamic programming approach to the solution of the problem.
Using a 3-dimensional list to store previous calculations.
'''
def solve(min_coins, C, n1, n5, n10):
    if min_coins[C][n5][n10] > 0:
        return min_coins[C][n5][n10]
    if C == 0:
        return 0

    ans = sys.maxsize
    if n10 > 0:
        ans = min(ans, 1 + solve(min_coins, C-1, n1+2, n5, n10-1))
    if n5 > 1:
        ans = min(ans, 2 + solve(min_coins, C-1, n1+2, n5-2, n10))
    if n5 and n1 > 2:
        ans = min(ans, 4 + solve(min_coins, C-1, n1-3, n5-1, n10))
    if n1 > 7:
        ans = min(ans, 8 + solve(min_coins, C-1, n1-8, n5, n10))
    if n10 and n1 > 2: # Inserting three ones and then a ten for a return of a fiver
        ans = min(ans, 4 + solve(min_coins, C-1, n1-3, n5+1, n10-1))
    min_coins[C][n5][n10] = ans
    return ans


def main():
    T = int(input())
    min_coins = [[[-1 for _ in range(51)]
                               for _ in range(151)]
                               for _ in range(151)]
    for i in range(T):
        C, n1, n5, n10 = map(int , input().split())
        print(solve(min_coins, C, n1, n5, n10))


if __name__ == "__main__":
    main()
