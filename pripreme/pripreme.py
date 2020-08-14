def main():
    '''
    Solution is based on finding the maximum value and checking wether
    it will be a choke in the process (wether idle time appears or not).

    In the case
    [1 2 4], team number three will be a choke on the process since the needed time
    will surpass that of rest, which implies that max > total // 2 which must imply
    that idle time will arise.

    In the case of [2 2 2], we will have no idle time since there does not exist a
    value for which idle time would arise.
    '''
    n = int(input())

    total = 0
    maximum = 0
    for i in input().split():
        total += int(i)
        maximum = max(int(i), maximum)

    rest = total - maximum
    print(2*maximum if rest < maximum else total)

if __name__ == "__main__":
    main()
