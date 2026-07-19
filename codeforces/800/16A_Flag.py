def sol():
  n, m = map(int, input().split())
  a = [input() for i in range(n)]
  check = -1
  for i in a:
    if len(set(i)) == 1 and check != i[0]:
      check = i[0]
    else:
      print("NO")
      break
  else:
    print("YES")

sol()
