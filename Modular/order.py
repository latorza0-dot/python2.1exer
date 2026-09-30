from menu import menu


def get_order():

    orders = []

    while True:

        item = input("\nEnter milk tea flavor: ").title()

        if item not in menu:
            print("Flavor not found. Please choose from the menu.")
            continue

        try:
            qty = int(input("Enter quantity: "))

            if qty <= 0:
                print("Quantity must be at least 1.")
                continue

        except ValueError:
            print("Please enter a valid number.")
            continue

        price = menu[item]

        orders.append([item, qty, price])

        again = input("Order another milk tea? (yes/no): ").lower()

        if again != "yes":
            break

    return orders


def get_total(orders):

    total = 0

    for order in orders:

        item = order[0]
        qty = order[1]
        price = order[2]

        total = total + (qty * price)

    return total
