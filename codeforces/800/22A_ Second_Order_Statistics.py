def sol():
  n = int(input())
  a = sorted(set(map(int, input().split())))
  if len(a) < 2:
    print("NO")
  else:
    print(a[1])

sol()
