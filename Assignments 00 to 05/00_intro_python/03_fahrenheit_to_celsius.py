def temp():
  print("This application for converting fahrenheit to celsius")
  fahrenheit_degree = float(input("Enter your fahrenheit degree "))
  celsius_degree = (fahrenheit_degree - 32) * 5.0/9.0
  print(f"Temprature {fahrenheit_degree} F = {celsius_degree} C")

if __name__ == "__main__":
 temp()
