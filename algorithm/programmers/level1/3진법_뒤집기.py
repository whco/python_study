def solution(n):
    ternary = []
    while(n):
        ternary.append(str(n % 3))
        n //= 3
    # return sum([3**(len(ternary) - 1 - i) * e for i, e in enumerate(ternary)])
    return int(''.join(ternary), 3)