def solution(num):
    count = 0
    while(num != 1 and count < 500):
        num = num / 2 if num % 2 == 0 else 3 * num + 1
        count += 1
    return count if num == 1 else -1