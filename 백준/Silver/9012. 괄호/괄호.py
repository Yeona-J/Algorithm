import sys
from collections import deque

n = int(input())
for i in range(n):
    vps = deque()
    test = sys.stdin.readline().strip()
    for j in test:
        if j == "(":
            vps.append(j)
        else:
            if len(vps) == 0:
                vps.append(j)
            else:
                if vps[-1] == "(":
                    vps.pop()
                else:
                    vps.append(j)
    if len(vps) == 0:
        print("YES")
    else:
        print("NO")