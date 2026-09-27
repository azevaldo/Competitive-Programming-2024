a = int(input())
b = input()
f = 0
l = 0
h = ""
c = 0
d = 2
e = b[c:d]
for i in range(a-1):
    g = 0
    c = 0
    d = 2
    for j in range(a-1):
        if e == b[c:d]:
            g += 1
        c += 1
        d += 1
    if g > l:
        l = g
        h = e
    f += 1
    e = b[f:f+2] if f < len(b) else 0
print(h)