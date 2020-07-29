def parse_data():
    N = int(input())
    sticks = input().split(' ')
    sticks = [int(x) for x in sticks]
    sticks.sort(key=lambda x : x)
    return sticks

def run(sticks):
    for i in range(0, len(sticks)):
        if i + 3 > len(sticks):
            break
        a,b,c = sticks[i:i+3]
        if a + b > c and a + c > b and b + c > a:
            print("possible")
            return
    print("impossible")

def main():
    sticks = parse_data()
    run(sticks)

if __name__ == "__main__":
    main()
