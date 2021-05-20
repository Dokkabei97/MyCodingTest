# N, M, K를 공백으로 구분하여 입력받기

n, m, k = map(int, input().split())

'''
N = 배열의 크기
M = 더하는 횟수
K = 더하는 횟수 최대 중복 수
'''

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()  # 입력 받은 수들 정렬하기
# print('data.sort = ', data)
first = data[n - 1] # 가장 큰 수
# print('first = ', first)
second = data[n - 2] # 두 번째로 큰 수
# print('second = ', second)

result = 0

while True:
    for i in range(k): # 가장 큰 수를 K번 더하기
        if m == 0: # m이 0이라면 반복문 탈출
            break
        result += first
        # print('result = ', result)
        m -= 1 # 더할 때마다 1씩 빼기
        # print('m = ', m)
    if m == 0: # m이 0이라면 반복문 탈출
        break
    result += second # 두 번째로 큰 수를 한 번 더하기
    # print('result2 = ', result)
    m -= 1 # 더할 때마다 1씩 빼기
    # print('m2 = ', m)

print(result)


