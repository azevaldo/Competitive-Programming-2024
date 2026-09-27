a = int(input())
for i in range(a):
    b = input().split(":")
    if 0 < int(b[0]) < 12:
        print(":".join(b)+" AM")
    elif 12 < int(b[0]) <= 21:
        print(f"0{int(b[0])-12}:{b[1]} PM")
    elif int(b[0]) > 21:
        print(f"{int(b[0]) - 12}:{b[1]} PM")
    elif int(b[0]) == 12:
        print(f"12:{b[1]} PM")
    else:
        print(f"12:{b[1]} AM")