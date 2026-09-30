from menu import show_menu
from order import get_order, get_total
from receipt import show_receipt


def main():

    print("================================")
    print("       WELCOME TO MILK TEA SHOP")
    print("================================")

    show_menu()

    answer = input("\nWould you like to order milk tea? (yes/no): ").lower()

    if answer != "yes":
        print("Thank you for visiting our Milk Tea Shop!")
        return

    orders = get_order()

    total = get_total(orders)

    # 10% discount for orders worth ₱500 or more
    if total >= 500:
        discount = total * 0.10
    else:
        discount = 0

    final = total - discount

    show_receipt(orders, total, discount, final)


main()
