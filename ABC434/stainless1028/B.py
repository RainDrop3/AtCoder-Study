import sys
input = lambda: sys.stdin.buffer.readline()#.decode("ascii").rstrip()
fprint = lambda s: sys.stdout.write(str(s) + "\n")
exit = lambda: sys.exit(0)

n, m = map(int, input().split())
total = [0] * (m + 1)
cnt = [0] * (m + 1)

for i in range(n):
    a, b = map(int, input().split())
    total[a] += b
    cnt[a] += 1

for i in range(1, m + 1):
    print(total[i] / cnt[i])
