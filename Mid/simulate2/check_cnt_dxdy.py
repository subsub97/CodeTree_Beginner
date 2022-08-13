n, m = map(int, input().split())

# n x n 행렬 만들어주기
grid = [
    [0] * n
    for _ in range(n)
]

cnt = 0


arr = [
    list(map(int, input().split()))
    for _ in range(m)]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

for i in range(m):
    a, b = arr[i][0], arr[i][1]
    a -= 1
    b -= 1
    grid[a][b] = 1

    for j in range(n):
        cnt = 0
        t_cnt = 0
        for dx, dy in zip(dxs, dys):
            # nx,ny 는 인접한 위치
            nx, ny = a + dx, b + dy
            if in_range(nx, ny) and grid[nx][ny] == 1:
                cnt += 1
        if cnt >= 3 and cnt < 4:
            t_cnt += 1
    print(t_cnt)
