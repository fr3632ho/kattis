# combinatorics

s=raw_input()
seen_? = seen_1 = seen_0 = 0
power=1
total=0
for char in s:
    if char == '?':

        seen_? += 1

    elif char== '1':

        seen_1 += 1

    else:
        seen_0 += 1
