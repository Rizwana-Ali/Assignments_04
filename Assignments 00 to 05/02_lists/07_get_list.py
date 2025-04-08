def main():
  lst = []
  val = input("Enter a value to add to the list. ")
  while val:
    lst.append(val)
    val = input("Enter a value to add to the list. ")
  print("Here's the list: ",lst)

if __name__ == "__main__":
  main()


