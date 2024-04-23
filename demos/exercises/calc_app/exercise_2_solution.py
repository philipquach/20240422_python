from typing import Any


def main() -> None:
    total: int | float = 0
    id: int = 0
    history: list[dict[str, Any]] = []

    # infinite loop
    while True:
        command = input("Enter a command: ")

        # capture user input from the command line
        if command == "add":
            operand = input("Please enter an operand: ")
            # "add" : operation to perform => +
            total += int(operand)
            id += 1
            # Add to history dictionary
            history.append({"id": id, "command": command, "operand": operand})
            print(f"Result: {total}")
        elif command == "subtract":
            operand = input("Please enter an operand: ")
            # "subtract" : operation to perform => -
            total -= int(operand)
            id += 1
            # Add to history dictionary
            history.append({"id": id, "command": command, "operand": operand})
            print(f"Result: {total}")
        elif command == "multiply":
            operand = input("Please enter an operand: ")
            # "multiply" : operation to perform => *
            total *= int(operand)
            id += 1
            # Add to history dictionary
            history.append({"id": id, "command": command, "operand": operand})
            print(f"Result: {total}")
        elif command == "divide":
            operand = input("Please enter an operand: ")
            # "divide" : operation to perform => /
            total /= float(operand)
            id += 1
            # Add to history dictionary
            history.append({"id": id, "command": command, "operand": operand})
            print(f"Result: {total}")
        elif command == "clear":
            # "clear" - reset current result to 0 - does not have an operand
            total = 0
            print(f"Result: {total}")
        elif command == "history":
            for line in history:
                print(
                    f"id: {line['id']}, command: {line['command']}, operand: {line['operand']}"
                )
        elif command == "exit":
            # break will exit the loop
            break
        else:
            # Unknown command
            print("Error: Unknown command")


if __name__ == "__main__":
    main()
