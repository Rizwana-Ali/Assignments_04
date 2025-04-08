def main():
    print("Welcome to the Planetary Weight Calculator")
    print('******************************************')

    try:
        earth_weight = float(input("Enter your weight on Earth (kg): "))
    except ValueError:
        print("Please enter a valid number for weight.")
        return

    gravity_ratios = {
        "Mercury": 0.38,
        "Venus": 0.91,
        "Mars": 0.38,
        "Jupiter": 2.34,
        "Saturn": 0.93,
        "Uranus": 0.92,
        "Neptune": 1.19
    }

    print("\nSelect a planet:")
    for planet in gravity_ratios:
        print(f"- {planet}")

    planet_choice = input("Enter the name of the planet: ").title()

    if planet_choice in gravity_ratios:
        new_weight = earth_weight * gravity_ratios[planet_choice]
        print(f"\nYour weight on {planet_choice} would be: {new_weight:.2f} kg")
    else:
        print("Invalid planet choice.")

if __name__ == "__main__":
    main()



