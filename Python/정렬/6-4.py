''''''

'''
퀵 정렬

'기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸면 어떨까?'

퀵 정렬은 기준을 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식으로 동작한다

퀵 정렬에서는 피벗(Pivot)이 사용된다. 큰 숫자와 작은 숫자를 교환할 때, 교환하기 위한 '기준'을 바로 피벗이라 표현한다
퀵 정렬을 수행하기 전에는 피벗을 어떻게 설정할 것인지 미리 명시해야한다. 피벗을 설정하고 리스트를 분한할하는 방법에 따라서
여러가지 방식으로 퀵 정렬을 구분하는데 대표적인 방식은 호어 분할(Hoare Partition)이 있다
호어 분할 방식에서는 다음과 같은 규칙에 따라서 피벗을 설정한다
'리스트에서 첫 번째 데이터를 피벗으로 정한다'
'''

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이더를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)
