def main() -> None:
    total: int | float = 0
    # infinite loop
    while True:
        # capture user input from the command line
        command = input("Enter a command: ")
        operand = input("Please enter an operand: ")

        if command == "add":
            # "add" : operation to perform => +
            total = total + int(operand)
        elif command == "subtract":
            # "subtract" : operation to perform => -
            total = total - int(operand)
        elif command == "multiply":
            # "multiply" : operation to perform => *
            total = total * int(operand)
        elif command == "divide":
            # "divide" : operation to perform => /
            total = total / float(operand)
        elif command == "clear":
            # "clear" - reset current result to 0 - does not have an operand
            total = 0
        elif command == "exit":
            # break will exit the loop
            break
        else:
            # Unknown command
            print("Error: Unknown command")

            # echo the command to the command line
            # f-string is a convenient way to format strings (string interpolation)
            print(f"Received command: {command}")
            print(f"Result: {total}")


if __name__ == "__main__":
    main()
