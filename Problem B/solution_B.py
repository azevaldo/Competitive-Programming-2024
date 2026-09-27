d = int(input())
for i in range(d):
    a, b, c = list(map(int, input().split()))
    if a < b < c:
        print("STAIR")
    elif a < b > c:
        print("PEAK")
    else:
        print("NONE")