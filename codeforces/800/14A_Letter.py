def sol():
  mxi, mni, mxc, mnc = -1, -1, -1, -1
  n, m = map(int, input().split())
  a = []
  for _ in range(n):
    a.append(input())
  for i, row in enumerate(a):
    if "*" in row:
      mxi = i
      if mni == -1:
        mni = i
  for i in a:
    if "*" in i:
      if mnc == -1 or i.index("*") < mnc:
        mnc = i.index("*")
  for i in a:
    if "*" in i:
      if mxc == -1 or i.rindex("*") > mxc:
        mxc = i.rindex("*")
  a = [i[mnc:mxc+1] for i in a[mni:mxi+1]]
  
  print(*a, sep="\n")

sol()
