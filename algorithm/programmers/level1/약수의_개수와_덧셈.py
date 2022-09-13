def solution(left, right):
    return (left + right) / 2 * (right - left + 1) - 2 * sum(i**2 for i in range(int(left**0.5), int(right**0.5) + 1))
