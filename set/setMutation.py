A = int(input())
N = set(map(int, input().split()))
for i in range(int(input())):
    a = input().split()
    n = set(map(int, input().split()))
    if a[0] == 'intersection_update':
        N.intersection_update(n)
    elif a[0] == 'update':
        N.update(n)
    elif a[0] == 'symmetric_difference_update':
        N.symmetric_difference_update(n)
    elif a[0] == 'difference_update':
        N.difference_update(n)

print(sum(N))
