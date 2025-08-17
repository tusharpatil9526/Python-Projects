portfolio = {}

while True:
    print("\n1. Add Stock\n2. View Portfolio\n3. Exit")
    choice = input("Choose (1-3): ")

    if choice == '1':
        name = input("Stock name: ").upper()
        quantity = int(input("Quantity: "))
        price = float(input("Price per share: "))
        
        if name in portfolio:
            portfolio[name][0] += quantity
            portfolio[name][1] = price
        else:
            portfolio[name] = [quantity, price]
        print(f"Added {quantity} shares of {name}.")

    elif choice == '2':
        total = 0
        print("\nYour Portfolio:")
        for stock, (quantity, price) in portfolio.items():
            value = quantity * price
            total += value
            print(f"{stock}: {quantity} shares at ${price:.2f} (Total: ${value:.2f})")
        print(f"Total Portfolio Value: ${total:.2f}")

    elif choice == '3':
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
