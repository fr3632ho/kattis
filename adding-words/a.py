# Time limit 1 sec
# calc commands
# def commands
# clear command

d = dict()
sum_d = dict()
while True:
    try:
        line = raw_input().split()
    except EOFError:
        exit(0)

    if line[0] == 'clear':
        d.clear()
        sum_d.clear()
        continue

    if line[0] == 'def':
        if line[1] in d:
            del sum_d[d[line[1]]]
        d[line[1]] = line[-1]
        sum_d[line[-1]] = line[1]
        continue

    out = [""]*(len(line)-1)
    value = [""]*(len(line)-1)
    flag = True
    for i in range(1, len(line), 2):
        v, o = line[i], line[i+1]
        out[i-1], out[i] = v, o
        if not v in d:
            flag = False
            continue
        if o == '=':
            value[i-1] = d[v]
        else:
            value[i-1], value[i] = d[v], o

    if not flag:
        out.append("unknown")
        print " ".join(out)
        continue


    sum = str(eval("".join(value)))
    if sum in sum_d:
        print " ".join(out), sum_d[sum]
    else:
        print " ".join(out), "unknown"
