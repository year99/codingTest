# 총 N개의 바구니
# 각각의 바구니에는 1번~N번까지 번호가 적혀있는 공을 매우 많이 가지고 있음.
# 가장 처음 바구니에는 공이 들어있지 않으며, 바구니에는 공을 1개만 넣을 수 있다.
# M번 공을 넣는다.
# 한 번 공을 넣을 때, 공을 넣을 바구니 범위를 정하고, 정한 바구니에 모두 같은 번호가 적혀있는 공을 넣는다.
# 만약 바구니에 공이 이미 있는 경우에는 들어있는 공을 빼고, 새로 공을 넣는다.
# 공을 어떻게 넣을지가 주어졌을 때, M번 공을 넣은 이후에 각 바구니에 어떤 공이 들어 있는지 구하는 프로그램 작성.

N, M = map(int,input().split())
# 5 4 -> 5개의 바구니, 1~5번까지 번호가 적혀있는 공을 매우 많이 가지고 이씅
# 4번 공을 넣는다

# 1번 바구니부터 5번 바구니에 들어있는 공의 번호를 공백으로 구분해 출력 / 공이 들어있찌 않은 바구니는 0을 출력

# i j k
basket = [0 for i in range(N+1)]
for n in range(M):
    i, j, k = map(int, input().split())
    for a in range(i, j+1):
        basket[a] = k
for _ in basket:
    print(_, end=" ")