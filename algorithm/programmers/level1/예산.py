def solution(d, budget):
    sum = 0
    for i, e in enumerate(sorted(d)):
        sum += e
        if sum > budget:
            return i
    return len(d)