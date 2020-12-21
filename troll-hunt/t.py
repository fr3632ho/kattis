bridges, knights, g_size = map(int, raw_input().split())
bridges -= 1
groups = knights//g_size
days = bridges // groups + 1*(bridges % groups != 0)
print days
