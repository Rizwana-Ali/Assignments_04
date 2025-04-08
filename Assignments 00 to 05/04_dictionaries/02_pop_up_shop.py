def calculate_total_cost():
    fruits_price = {'banana': 1.5, 'strawbarrires': 50, 'apple': 80, 'grapes': 1, 'mangoes': 1.5, 'guava': 5}

    total_cost = 0
    for fruit_name in fruits_price:
        price = fruits_price[fruit_name]
        amount_bought = int(input("How many (" + fruit_name + ") do you want to buy?: "))
        total_cost += (price * amount_bought)

    print("Your total cost is $" + str(total_cost))


if __name__ == '__main__':
    calculate_total_cost()