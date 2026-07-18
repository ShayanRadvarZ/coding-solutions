def sol(a: list[str]) -> None:
  b = [row[::-1] for row in a[::-1]]
  if a == b:
    print("YES")
  else:
    print("NO")

a = [input().strip() for _ in range(3)]

if __name__ == "__main__":
  sol(a)
