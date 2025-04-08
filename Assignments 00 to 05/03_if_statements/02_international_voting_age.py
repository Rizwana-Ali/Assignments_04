Peturksbouipo_age:int = 16
Stanlau_age:int = 25
Mayengua_age:int = 48

def main():

    user_age = int(input("How old are you? "))


    if user_age >= Peturksbouipo_age:
        print(f"you are eligible to vote in  Peturksbouipo where the voting age is {Peturksbouipo_age} .")
    else:
        print(f"you are not eligible to vote in  Peturksbouipo where the voting age is {Peturksbouipo_age} .")


    if user_age >= Stanlau_age:
        print(f"you are eligible to vote in Stanlau  where the voting age is {Stanlau_age} .")
    else:
        print(f"you are not eligible to vote in Stanlau  where the voting age is {Stanlau_age} .")


    if user_age >= Mayengua_age:
        print(f"you are eligible to vote in Mayengua  where the voting age is {Mayengua_age} .")
    else:
        print(f"you are not eligible to vote in Mayengua  where the voting age is {Mayengua_age} .")




if __name__ == '__main__':
    main()