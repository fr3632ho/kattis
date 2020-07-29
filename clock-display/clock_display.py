import sys
import numbers

zero  = ["+---+", "|   |", "|   |", "+   +", "|   |", "|   |", "+---+"]
one   = ["    +", "    |", "    |", "    +", "    |", "    |", "    +"]
two   = ["+---+", "    |", "    |", "+---+", "|    ", "|    ", "+---+"]
three = ["+---+", "    |", "    |", "+---+", "    |", "    |", "+---+"]
four  = ["+   +", "|   |", "|   |", "+---+", "    |", "    |", "    +"]
five  = ["+---+", "|    ", "|    ", "+---+", "    |", "    |", "+---+"]
six   = ["+---+", "|    ", "|    ", "+---+", "|   |", "|   |", "+---+"]
seven = ["+---+", "    |", "    |", "    +", "    |", "    |", "    +"]
eight = ["+---+", "|   |", "|   |", "+---+", "|   |", "|   |", "+---+"]
nine  = ["+---+", "|   |", "|   |", "+---+", "    |", "    |", "+---+"]

nbrs = { '1' : one,
                   '2' : two,
                   '3' : three,
                   '4' : four,
                   '5' : five,
                   '6' : six,
                   '7' : seven,
                   '8' : eight,
                   '9' : nine,
                   '0' : zero}

def print_time(line):
    s = '  '
    words = line.split(':')
    t1,t2,t3,t4 = nbrs[words[0][0]],nbrs[words[0][1]],nbrs[words[1][0]],nbrs[words[1][1]]
    for i in range(0,len(t1)):
        s = 'o' if (i == 2 or i == 4) else ' '
        print(f'{t1[i]}  {t2[i]}  {s}  {t3[i]}  {t4[i]}')
    print('\n')

def print_times(data):
    for line in data:
        if line == 'end':
            print(line)
            break
        print_time(line)

if __name__ == "__main__":
    input = sys.stdin.read().rstrip('\n').split('\n')
    print_times(input)
