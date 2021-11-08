# 標準入力を受け付ける。
N = int(input())

# 各技(1~N)を習得するために必要な時間を管理する。
# T[0]は利用しない。
T = [0] * (N + 1)
# 各技(1~N)を習得するために、習得しておくべき技の情報を管理する。
# A[0]は利用しない。
A = [[]] * (N + 1)

for i in range(1, N + 1):
    X = list(map(int, input().split()))
    T[i] = X[0]
    A[i] = X[2:]

# need_list : 技Nを習得するために、必要な技を管理する。
# need_list[idx] = True : 技Nを習得するために、技idxを習得する必要がある。
# need_list[idx] = False : 技Nを習得するために、技idxを習得する必要がない。
# need_list[0]は利用しない。
need_list = [False] * (N + 1)
# 技Nは習得することが決まっているので、Trueと初期化する。
need_list[len(need_list) - 1] = True

# 新しい技の習得に紐づく、習得しておくべき技情報は、習得しておくべき技情報 < 新しい技の関係であるため、以下のようなfor文が実現できる。
for n in range(N, 0, -1):
    if not need_list[n]:
        continue

    # 技nを習得するために、習得しておくべき技に関してTrueに変更する。
    for child in A[n]:
        need_list[child] = True

ans = 0
for i in range(1, N + 1):
    if need_list[i]:
        ans += T[i]

print(ans)
