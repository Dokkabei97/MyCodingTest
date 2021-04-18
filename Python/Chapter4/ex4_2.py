'''
시각
난이도 1, 풀이 시간 15분, 시간 제한 2초, 메모리 제한 128mb
'''
# H를 입력받기
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운드 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)