# 파이썬의 정렬 라이브러리

'''
파이썬은 기본 정렬 라이브러리인 sorted() 함수를 제공한다
sorted()는 퀵 정렬과 동작 방식이 비슷한 병합 정렬을 기반으로 만들어졌는데, 병합 정렬은 일반적으로 퀵 정렬보다
느리지만 최악의 경우에도 시각 복잡도를 보장하는 특징이 있다
'''

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array)
print(result)
