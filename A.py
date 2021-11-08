# 標準入力を受け付ける。
X = input()

# 小数点より前の数字と後ろの数字に分離する。
front, back = X.split('.')

# 後ろの数字の先頭文字が0~4ならば、前の数字を出力する。そうでなければ前の数字に+1して出力する。
if int(back[0]) >= 0 and int(back[0]) <= 4:
    print(front)
else:
    print(int(front) + 1)
