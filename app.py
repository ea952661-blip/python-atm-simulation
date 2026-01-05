balance = 1000

while True:
    user_pin = input("Set your 4-digit PIN code: ")
    if len(user_pin) == 4 and user_pin.isdigit():
        print("PIN set successfully!\n")
        break
    else:
        print("PIN is invalid! Make sure PIN is exactly 4 digits.")

attempts = 0
while attempts < 3:
    pin_input = input("Enter your PIN code to access the ATM: ")
    if pin_input == user_pin:
        print("PIN accepted! Welcome to Bank of Python.\n")
        break
    else:
        attempts += 1
        print("Incorrect PIN! Attempts left:", 3 - attempts)
else:
    print("Too many wrong attempts. Card blocked!")
    exit()

while True:
    print("\n=== ATM Menu ===")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit ATM Menu")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("Your balance is:", balance)

    elif choice == "2":
        amount = int(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Enter a positive amount!")
        elif amount > balance:
            print("Not enough balance!")
        else:
            balance -= amount
            print("Withdrawal successful! New balance is:", balance)

    elif choice == "3":
        amount = int(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Enter a positive amount!")
        else:
            balance += amount
            print("Deposit successful! New balance is:", balance)

    elif choice == "4":
        print("Thanks for using Bank of Python! Please take your card!")
        break

    else:
        print("Invalid choice, please try again.")
