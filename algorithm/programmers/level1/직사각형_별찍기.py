a, b = map(int, input().strip().split(' '))
# print(('*' * a + '\n') * b)
print('\n'.join(['*' * a] * b))