from math import gcd
def sol():
  Y , W = map(int, (input()).split())
  greatest = Y if Y > W else W
  num = 7 - greatest
  den = 6
  g = gcd(num, den)
  print(f"{num // g}/{den // g}")
if __name__ == "__main__":
  sol()
# Could have hard coded a list with all of the possible outcomes (7 possible outcomes)
