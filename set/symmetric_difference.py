n = int(input())
stn = set(map(int, input().split()))
b = int(input())
stb = set(map(int, input().split()))
stu = stn.symmetric_difference(stb)
print(len(stu))
