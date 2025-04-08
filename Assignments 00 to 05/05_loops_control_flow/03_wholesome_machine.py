correct_affermation =  "I am capable of doing anything. I put mymind too."

def main():
  print("Welcome to the Wholesome Mashine")
  while True:
    user_input = input("Please type the following affermation:" + correct_affermation)
    if user_input == correct_affermation:
      print("That\'s right! ")
      break
    else:
      print("Humm that was not the affermation. Please Try  Again!")

if __name__ == "__main__":
  main()


