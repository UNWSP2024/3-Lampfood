#Elliott Morris, 1/20/2026, Hot Dog Calculator
#This program asks the user what hot dog type and toppings they want and calculates the total


def hot_dog_calculator():
    #Prices
    HOT_DOG_PRICE = 3.50
    CHILLI_DOG_PRICE = 4.50
    CHEESE_PRICE = 3.50
    PEPPERS_PRICE = 3.50
    ONIONS_PRICE = 1.00
    TAX_RATE = 0.07

    #input hotdog type
    while True:
        hot_dog_type = input("Enter hot dog type (Hot Dog or Chilli Dog): ").strip().lower()
        if hot_dog_type == "hot dog":
            base_price = HOT_DOG_PRICE
            break
        elif hot_dog_type == "chilli dog":
            base_price = CHILLI_DOG_PRICE
            break
        else:
            print("Invalid hot dog type")

    #input optional toppings
    cheese = input("Add cheese? (Y/N): ").strip().lower()
    peppers = input("Add peppers? (Y/N): ").strip().lower()
    onions = input("Add onions? (Y/N): ").strip().lower()

    #calculate topping cost
    topping_cost = 0
    if cheese == "y":
        topping_cost += CHEESE_PRICE
    if peppers == "y":
        topping_cost += PEPPERS_PRICE
    if onions == "y":
        topping_cost += ONIONS_PRICE

    #calculate final price
    subtotal = base_price + topping_cost
    tax = subtotal * TAX_RATE
    total = subtotal + tax

    #display receipt
    print("\n---- Receipt ----")
    print(f"Hot Dog Price: ${subtotal:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total Cost: ${total:.2f}")


if __name__ == "__main__":
    hot_dog_calculator()
