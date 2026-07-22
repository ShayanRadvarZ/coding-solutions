def sol():
  mp = {
      "." : "0",
      "-." : "1",
      "--" : "2"
      }
 
  a = input()
  n = 0
  ans = []

  while n < len(a):
    if a[n] == ".":
      n += 1
      ans.append(mp["."])
    else:
      ans.append(mp[a[n:n+2]])
      n += 2
  print("".join(ans))

sol()
