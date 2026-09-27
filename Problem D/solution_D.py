d = int(input())
for i in range(d):
    a = input()
    b, c = a.count("A"), a.count("B")
    print("A" if b > c else "B")