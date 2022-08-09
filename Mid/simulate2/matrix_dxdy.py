# # 격자에서의 dx,dy 란 행렬에서의 x,y 를 의미한다
# # 그렇기 때문에 평면좌표상의 x,y 증감식과는 방향이 다르다
#
# n = int(input())
#
# arr = [
#     tuple(map(int, input().split()))
#     for i in range(n)
# ]
#
#
# # (x,y)가 격자 내에 있는지를 판단해주는 함수
# # 안에 있다면 True / 안에 없다면 False 반환
# def in_range(x, y):
#     return 0 <= x and x < 5 and 0 <= y and y < 5
#
#
# for dir_num in range(4):
#     # 인접한 칸의 위치 nx,ny
#     nx, ny = x + dx[dir_num], y + dy[dir_num]
#     # nx, ny = 3, 1
#     # in_range() 함수를 이용하여 index Error를 막는 방어함수
#     # if문에서의 and 로 연결된 조건은 왼쪽부터 확인한다
#     # 따라서 왼쪽부터 확인된 조건이 False라면 뒤는 확인조차 안한다
#     # 그래서 아래 if문의 조건을 a[nx][ny]를 먼저 선행조건으로 바꾼다면
#     # RunTime error 가 발생한다 . 없는 인덱스를 확인하라고 했기에 !!
#     if in_range(nx, ny) and a[nx][ny] == 1:
#         cnt += 1
#
#     # zip() 함수는?
#     '''
#     2개의 리스트를 한번에 인자들에게 자신의 원소를
#     넘겨 줄 수 있다.
#     ex)
#     dxs = [1,0,-1,0] dys = [0,1,0,-1]
#     for dx,dy in zip(dxs,dys)
#     순선대로
#     dx = 1 , dy = 0
#     dx = 0 , dy = 1
#     dx = -1, dy = 0
#     dx = 0 , dy = -1
#     이 입력된다.
#     '''

n = int(input())

matrix = [
    list(map(int, input().split()))
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n
    # 위처럼 작성한다면


# 행렬/격자에서의 x,y
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

# 1의 개수를 세어줄 count 변수

t_cnt = 0

for x in range(n):
    for y in range(n):
        cnt = 0
        for dx, dz in zip(dxs, dys):
            # nx,ny 는 인접한 위치
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and matrix[nx][ny] == 1:
                cnt += 1

        if cnt >= 3:
            t_cnt += 1
print(t_cnt)
