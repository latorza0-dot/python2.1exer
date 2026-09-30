def show_receipt(orders, total, discount, final):

    print("\n")
    print("========================================")
    print("          MILK TEA SHOP")
    print("            YOUR RECEIPT")
    print("========================================")

    print("Item\t\t\tQty\tPrice\tTotal")
    print("----------------------------------------")

    for order in orders:

        item = order[0]
        qty = order[1]
        price = order[2]

        item_total = qty * price

        print(item, "\t", qty, "\t", price, "\t", item_total)

    print("----------------------------------------")
    print("Subtotal: PHP", total)
    print("Discount: PHP", discount)
    print("TOTAL:    PHP", final)
    print("========================================")
    print("      Thank you for ordering!")
    print("        Enjoy your milk tea!")
    print("========================================")
