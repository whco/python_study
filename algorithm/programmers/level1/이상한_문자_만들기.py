def solution(s):
    return ' '.join(map(lambda x : ''.join(c.lower() if i % 2 else c.upper() for i, c in enumerate(x)), s.split(' ')))
