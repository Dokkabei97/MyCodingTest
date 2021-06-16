print("금액을 입력하세요: ")
money = int(input())
n = 0

unit = [50000, 10000, 1000, 500, 100, 50, 10, 1]

for i in unit:
    n = money // i
    money %= i
    if n != 0:
        print(i, "원 짜리 :", n, "개")