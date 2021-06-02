''''''
'''
정렬 (Sorting)이란 데이터를 특정한 기준에 따라서 순서대로 나열하는 것을 말한다

정렬 알고리즘으로 데이터를 정렬하면 이진 탐색 (Binary Search)이 가능하다
정렬 알고리즘은 이진 탐색의 전처리 과정이기도 하다

정렬 알고리즘은
- 선택 정렬
- 삽입 정렬
- 퀵 정렬
- 계수 정렬 등이 있다
'''


'''
선택 정렬

데이터가 무작위로 여러 개 있을때, 이중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그다음 작은 데이터를 
선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복한다

'''

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프

print(array)