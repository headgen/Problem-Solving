target = int(input()) # target은 10의 배수

cnt = 0

for coin in (500, 100, 50, 10):
    num = target // coin
    cnt += num
    target -= coin * num


print(cnt)
