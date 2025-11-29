import sys
input = lambda: sys.stdin.buffer.readline()#.decode("ascii").rstrip()
fprint = lambda s: sys.stdout.write(str(s) + "\n")
exit = lambda: sys.exit(0)

w, b = map(int, input().split())
w *= 1000
print(w // b + 1)
