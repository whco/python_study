def solution(n, arr1, arr2):
    return [(''.join(['#' if c == '1' else ' ' for c in format(e1 | e2 , 'b').rjust(n, '0')])) for e1, e2 in zip(arr1, arr2)]