heights = [int(input()) for _ in range(9)]
heights.sort()
tot = sum(heights)

def f():
    for i in range(8): # ?? 9로하면 안된다는데 이해안감
        for j in range(i+1, 9):
            if tot - heights[i] - heights[j] == 100: # 이 if문에 들어오게되면 출력 후 끝(return)
                for k in range(9):
                    if i != k and j != k:
                        print(heights[k])
                return

f()