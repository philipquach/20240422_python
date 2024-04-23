from typing import Any


def prompt_input(prompt: str) -> str:
    return input(prompt)


def calculate_operand(command: str, result: float) -> Any:
    operand = int(prompt_input("Please enter an operand: "))
    if command == "add":
        result += float(operand)

    if command == "subtract":
        result -= float(operand)

    if command == "multiply":
        result *= float(operand)

    if command == "divide":
        result /= float(operand)

    return result


def calculate_history(
    command: str, total: float, id: int, history: list
) -> Any:
    id += 1
    # Add to history dictionary
    history.append({"id": id, "command": command, "operand": total})
    print(f"Result: {total}")


def main() -> None:
    total: int | float = 0
    id: int = 0
    history: list[dict[str, Any]] = []

    # infinite loop
    while True:
        command = prompt_input("Enter a command: ")

        # capture user input from the command line
        if command == "add":
            total = calculate_operand(command, total)
            calculate_history(command, total, id, history)

        elif command == "subtract":
            total = calculate_operand(command, total)
            calculate_history(command, total, id, history)
        elif command == "multiply":
            total = calculate_operand(command, total)
            calculate_history(command, total, id, history)
        elif command == "divide":
            total = calculate_operand(command, total)
            calculate_history(command, total, id, history)
        elif command == "clear":
            # "clear" - reset current result to 0 - does not have an operand
            total = 0
            print(f"Result: {total}")
            history.clear()
        elif command == "history":
            for line in history:
                print(
                    f"id: {line['id']}, command: {line['command']}, operand: {line['operand']}"
                )
        elif command == "remove":
            remove = input("Please enter id to remove: ")
            remove_id = int(remove)
            # print(history)
            for entry in history:
                if entry["id"] == remove_id:
                    print(entry["id"])
                    history.remove(entry)
                    break
            print(history)
        elif command == "exit":
            # break will exit the loop
            break
        else:
            # Unknown command
            print("Error: Unknown command")


if __name__ == "__main__":
    main()
