inch: int = 12

def foot():
    feet: int = int(input("Enter number of feet and I will convert into inches: "))
    print(f"That are {inch * feet} inches in {feet} feet!")


if __name__ == '__main__':
    foot()