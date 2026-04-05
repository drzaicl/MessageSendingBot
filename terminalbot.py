import time

print("====  This is a bot for automatic message sending  ====")

while True:

    choise = input("Please choose an option:\n1. Send Message \n2. Exit ")

    if choise == "1":
        message = input("Please enter your message: ")
        times = int(input("Please enter how many times you want to send: "))
        who = input("Please enter discord username: ")
        delay = int(input("Please enter delay between messages (seconds): "))

        while True:
            print("\n=== PREVIEW ===")
            print(f"Message: {message}")
            print(f"Times: {times}")
            print(f"Target: {who}")
            print(f"Delay: {delay}s")

            confirmation = input("\nSend this message? (y/n): ")

            if confirmation == "y":
                print("\nSending...\n")
                for i in range(times):
                    print(f"To {who}: {message}")
                    time.sleep(delay)
                print("\nDone!\n")
                break

            elif confirmation == "n":
                print("\nWhat do you want to change?")
                print("1. Message")
                print("2. Times")
                print("3. Target")
                print("4. Delay")
                print("5. Cancel")

                edit = input("Choose option: ")

                if edit == "1":
                    message = input("New message: ")

                elif edit == "2":
                    times = int(input("New times: "))

                elif edit == "3":
                    who = input("New target: ")

                elif edit == "4":
                    delay = int(input("New delay: "))

                elif edit == "5":
                    print("Cancelled.\n")
                    break

            else:
                print("Invalid input!")

    elif choise == "2":
        break

    else:
        print("Invalid option!")