menu = {
    "Classic Milk Tea": 80,
    "Wintermelon Milk Tea": 90,
    "Taro Milk Tea": 100,
    "Matcha Milk Tea": 110,
    "Brown Sugar Milk Tea": 120
}


def show_menu():

    print("\n========== MILK TEA MENU ==========")

    num = 1

    for item, price in menu.items():
        print(num, ".", item, "- PHP", price)
        num += 1

    print("===================================")
