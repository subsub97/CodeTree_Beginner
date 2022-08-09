# dx,dy 테크닉
if dir_num == 0:
    nx,ny = x + 1, y
elif dir_num == 1:
    nx,ny = x, y-1
elif dir_num == 2:
    nx,ny = x -1 , y
else:
    nx,ny = x, y + 1

'''
비슷한 코드를 여러줄에 적을경우
실수할 확률이 올라간다.
'''

dx = [1, 0 , -1, 0]
dy = [0, -1, 0, 1]

if dir_num == 0:
    nx,ny = x + dx[0], y + dy[0]
elif dir_num == 1:
    nx,ny = x + dx[1], y + dy[1]
elif dir_num == 2:
    nx,ny = x + dx[2] , y + dy[2]
else:
    nx,ny = x + dx[3], y + dy[3]

'''
이렇게 코드를 작성함으로써 index랑 
입력 받아지는 수랑 동일한 규칙이 생겼다.
따라서 더 효율적으로 만들수 있다.
'''

nx,ny = x + dx[dir_num], y + dy[dir_num]



