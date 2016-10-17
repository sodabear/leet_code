import sys

a = sys.stdin.readlines()
# b = int(a[0]) + int(a[1])
ans = 0
for x in a:
	ans = ans + int(x)
print(ans)