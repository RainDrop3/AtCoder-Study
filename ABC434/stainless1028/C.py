import sys
print(sys.version)
input = lambda: sys.stdin.buffer.readline()
fprint = lambda s: sys.stdout.write(str(s) + "\n")

for _ in range(int(input())):
    n, h = map(int, input().split())
    lowest, highest = h, h
    prev_t = 0
    flag = True
    for __ in range(n):
        t, l, u = map(int, input().split())
        if not flag:
            continue

        dt = t - prev_t
        highest = min(highest + dt, u)
        lowest = max(lowest - dt, l)

        if lowest > highest:
            flag = False
        prev_t = t

    fprint("Yes" if flag else "No")
