from milkteashop import Restaurant


def main():

    print("================================")
    print("       WELCOME TO MILK TEA SHOP")
    print("================================")

    shop = Restaurant()

    shop.show_menu()

    answer = input("\nWould you like to order milk tea? (yes/no): ").lower()

    if answer != "yes":
        print("\nThank you for visiting our Milk Tea Shop!")
        return

    shop.get_order()

    total = shop.get_total()

    if total >= 500:
        discount = total * 0.10
    else:
        discount = 0

    final = total - discount

    shop.show_receipt(total, discount, final)


main()
