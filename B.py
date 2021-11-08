# 標準入力を受け付ける。
N = int(input())

ans = set()
for _ in range(N):
    x = list(map(int, input().split()))
    # set型を利用すると、自動的に重複削除される。
    # list型で格納すると、エラーが発生するためstr型で格納する。
    ans.add(str(x[1:]))

print(len(ans))
