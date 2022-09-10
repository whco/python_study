def solution(n):
    if n ** 0.5 % 1 == 0:
        return n + 1 + 2 * n ** 0.5
    return -1
