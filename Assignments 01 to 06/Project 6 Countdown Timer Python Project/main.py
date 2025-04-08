import time
import sys

def main():
    while True:
        try:
            user_input = int(input("Enter the countdown duration in seconds: "))
            if user_input < 0:
                print("Invalid input. Please enter a positive number of seconds.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number of seconds.")

    for i in range(user_input, 0, -1):
        print(f"Time left: {i} seconds.", end="\r", flush=True)
        time.sleep(1)

    
    print("\nTime's up!")


if __name__ == "__main__":
    main()
