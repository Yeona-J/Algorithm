from itertools import combinations

N, M = map(int, input().split())
houses = []
chickens = []
for i in range(N):
    for j,v in enumerate(map(int,input().split())):
        if v == 1:
            houses.append((i,j))
        elif v == 2:
            chickens.append((i,j))

ans = 2 * N * len(houses)
for combi in combinations(chickens,M):
    tot = 0

    ans = min(ans,tot)

print(ans)