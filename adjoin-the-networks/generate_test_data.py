import sys

with open("test-cases/7.in", 'a') as file_1:
    file_1.truncate(0)
    file_1.write("100000 99999\n")

    for i in range(99999):
        file_1.write("{} {}\n".format(i, i+1))

with open("test-cases/8.in", 'a') as file_2:
    file_2.truncate(0)
    file_2.write("100000 99999\n")

    j = 0
    for i in range(99999+15000):
        if j == 1000:
            file_2.write("{} {}\n".format(i, i-j))
            j = 0
        j+=1
        file_2.write("{} {}\n".format(i, i+1))
