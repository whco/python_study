def solution(price, money, count):
    return max(price * count / 2 * (count + 1) - money, 0)