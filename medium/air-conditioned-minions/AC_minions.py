import sys

'''
Calculates the required number of rooms using a stack, the inner loop acts
as the number of minions that are possible to cram into one room.
Having the preference list sorted on lower bound gives us a way to accomodate each
minion with similar preferences.
'''
def calculate_rooms(pref,n):
    counter = 0
    # Take out one minion from the stack and cram in as many minions as possible with similar preferences.
    while pref:
        counter += 1
        a,b = pref.pop()

        # Cramming
        while pref and (a <= pref[-1][0] <= b or a <= pref[-1][1] <= b):
            a_prime,b_prime = pref.pop()
            a = max(a,a_prime)
            b = min(b,b_prime)
    return counter


if __name__ == "__main__":
    data = []
    for i in sys.stdin:
        data.append(i.strip())
    n = int(data[0])
    preferences = [[int(i) for i in line.split()] for line in data[1:]]
    preferences.sort(key=lambda x : x[0], reverse=True)
    print(calculate_rooms(preferences,n))
