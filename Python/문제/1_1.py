unit = [50000, 10000, 1000, 500, 100, 50, 10, 1]
info = {}

money = int(input("금액 입력 : "))
for u in unit:
    while money - u >= 0:
        if u in info:
            info[u] += 1
        else:
            info[u] = 1
        money = money - u

for i in info:
    print("{}원 짜리 : {}개".format(i, info[i]))