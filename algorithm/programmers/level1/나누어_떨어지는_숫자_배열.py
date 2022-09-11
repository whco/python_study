def solution(arr, divisor):
    return sorted([e for e in arr if e % divisor == 0]) or [-1]