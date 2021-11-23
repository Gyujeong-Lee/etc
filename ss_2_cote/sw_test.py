'''
포를 최대 세 번 움직여
잡을 수 있는 장기 알의 개수를 출력하라

1
5
0 1 0 0 1
1 1 0 0 0
0 1 1 0 1
0 0 2 0 0
1 0 1 1 0
'''
#갈 수 있는 좌표
def go(r, c):
    global N
    global new_location
    for i in range(1, N-1):
        #같은 행 비교
        if board[r][i] == 1:
            if i < c:
                cnt = 0
                while i > 0:
                    #다음 칸도 돌맹이라면,,,
                    if board[r][i-1] == 1:
                        cnt += 1
                    if cnt >= 2:
                        break
                    if [r, i-1] not in new_location:
                        new_location.append([r, i - 1])
                    i -= 1
            elif i > c:
                cnt = 0
                while i < (N - 1):
                    #다음 칸도 돌맹이라면,,,
                    if board[r][i+1] == 1:
                        cnt += 1
                    if cnt >= 2:
                        break
                    if [r, i + 1] not in new_location:
                        new_location.append([r, i + 1])
                    i += 1

    for i in range(1, N-1):
        if board[i][c] == 1:
            if i < r:
                cnt = 0
                while i > 0:
                    #다음 칸도 돌맹이라면,,,
                    if board[i-1][c] == 1:
                        cnt += 1
                    #두 개 이상의 돌맹이를 건너 뛸 순 없음
                    if cnt >= 2:
                        break

                    if [i - 1, c] not in new_location:
                        new_location.append([i - 1, c])

                    i -= 1
            elif i > r:
                cnt = 0
                while i < (N - 1):
                    #다음 칸도 돌맹이라면,,,
                    if board[i+1][c] == 1:
                        cnt += 1
                    if cnt >= 2:
                        break
                    if [i + 1, c] not in new_location:
                        new_location.append([i + 1, c])
                    i += 1
    return


T = int(input())

for tc in range(1, T+1):
    #없는 경우 0
    answer = 0
    #장기판 크기
    N = int(input())
    #장기알과 포
    board = []
    #가능한 좌표
    new_location = []

    for _ in range(N):
        board.append(list(map(int, input().split())))

    #1회 이동
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                go(i, j)

    #2회 이동
    l = len(new_location)
    for i in range(l):
        go(new_location[i][0], new_location[i][1])

    #3회 이동
    new_l = len(new_location)
    if l != new_l:
        for i in range(l, new_l):
            go(new_location[i][0], new_location[i][1])

    for i in range(len(new_location)):
        r = new_location[i][0]
        c = new_location[i][1]
        if board[r][c] == 1:
            answer += 1

    print('#{} {}'.format(tc, answer))


'''
0 1 0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0
0 1 1 0 1 0 0 1 0 0
0 0 0 0 1 0 0 0 0 0
0 1 1 0 0 0 0 0 0 0
0 0 0 0 2 0 1 0 1 0
0 0 0 0 0 0 1 0 0 0
1 0 1 1 0 0 1 0 0 0
0 0 0 0 0 0 0 0 1 0
0 1 0 0 1 0 1 1 0 0

'''