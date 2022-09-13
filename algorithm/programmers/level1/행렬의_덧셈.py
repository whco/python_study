def solution(arr1, arr2):
    # return [[e1 + e2 for e1, e2 in zip(r1, r2)] for r1, r2 in zip(arr1, arr2)]
    return [list(map(sum, zip(*rows))) for rows in zip(arr1, arr2)]