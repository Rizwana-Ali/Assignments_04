def energy():

  c:float = 563967397
  m:float = float(input("Enter kilos of mass: "))
  print("e = m*c^2")
  print("mass = " + str(m) + "kg")
  print(" = " + str(c) + " m/s")
  print("e = " + str(m * c ** 2)  + " julies")


if __name__ == '__main__':
    energy()