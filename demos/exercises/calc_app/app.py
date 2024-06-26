def main() -> None:
    total: int | float = 0

    # infinite loop
    while True:
        command = input("Enter a command: ")

        # capture user input from the command line
        if command == "add":
            operand = input("Please enter an operand: ")
            # "add" : operation to perform => +
            total += int(operand)
            print(f"Result: {total}")
        elif command == "subtract":
            operand = input("Please enter an operand: ")
            # "subtract" : operation to perform => -
            total -= int(operand)
            print(f"Result: {total}")
        elif command == "multiply":
            operand = input("Please enter an operand: ")
            # "multiply" : operation to perform => *
            total *= int(operand)
            print(f"Result: {total}")
        elif command == "divide":
            operand = input("Please enter an operand: ")
            # "divide" : operation to perform => /
            total /= float(operand)
            print(f"Result: {total}")
        elif command == "clear":
            # "clear" - reset current result to 0 - does not have an operand
            total = 0
            print(f"Result: {total}")
        elif command == "exit":
            # break will exit the loop
            break
        else:
            # Unknown command
            print("Error: Unknown command")


if __name__ == "__main__":
    main()
