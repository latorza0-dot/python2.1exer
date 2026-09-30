class Restaurant:

    def __init__(self):

        self.menu = {
            "Classic Milk Tea": 80,
            "Wintermelon Milk Tea": 90,
            "Taro Milk Tea": 100,
            "Matcha Milk Tea": 110,
            "Brown Sugar Milk Tea": 120
        }

        self.orders = []


    def show_menu(self):

        print("\n========== MILK TEA MENU ==========")

        num = 1

        for item, price in self.menu.items():
            print(num, ".", item, "- PHP", price)
            num += 1

        print("===================================")


    def get_order(self):

        while True:

            item = input("\nEnter milk tea flavor: ").title()

            if item not in self.menu:
                print("Flavor not found. Please try again.")
                continue

            try:
                qty = int(input("Enter quantity: "))

                if qty <= 0:
                    print("Quantity must be at least 1.")
                    continue

            except ValueError:
                print("Please enter a valid quantity.")
                continue

            price = self.menu[item]

            self.orders.append([item, qty, price])

            again = input(
                "Do you want to order another milk tea? (yes/no): "
            ).lower()

            if again != "yes":
                break


    def get_total(self):

        total = 0

        for order in self.orders:

            qty = order[1]
            price = order[2]

            total = total + (qty * price)

        return total


    def show_receipt(self, total, discount, final):

        print("\n")
        print("========================================")
        print("          MILK TEA SHOP")
        print("            YOUR RECEIPT")
        print("========================================")

        print("Item\t\t\tQty\tPrice\tTotal")
        print("----------------------------------------")

        for order in self.orders:

            item = order[0]
            qty = order[1]
            price = order[2]

            item_total = qty * price

            print(
                item, "\t",
                qty, "\t",
                price, "\t",
                item_total
            )

        print("----------------------------------------")
        print("Subtotal: PHP", total)
        print("Discount: PHP", discount)
        print("TOTAL:    PHP", final)

        print("========================================")
        print("     Thank you for ordering!")
        print("       Enjoy your milk tea!")
        print("========================================")
