from collections import deque

dy = (0,1,0,-1)
dx = (1,0,-1,0)
N, M = map(input().split())
board = [input() for _ in range(N)]

def is_valid_coord(y,x):
    return 0 <= y < N and 0 <= x < M
def bfs():
    chk = [[False] * M for _ in range(N)]
    chk[0][0] = True
    dq = deque()
    dq.append((0,0))
    while dq:
        y, x = dq.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = y + dx[k]
            if is_valid_coord(ny,nx) and board[ny][nx] == '1' and not chk[ny][nx]:
                chk[ny][nx] = True
                dq.append((ny,nx))




bfs()