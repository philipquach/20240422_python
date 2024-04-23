def num_input() -> int:
    return int(input("Enter a number: "))

                    # int = return type
def another_num_input() -> int:
    return int(input("Enter a number: "))


def prompt_num_input(prompt: str) -> int:
    return int(input(prompt))


def sum_numbers(a: int, b: int) -> int:
    return a + b


# Type hints is good for few bugs
def main() -> None:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a another number: "))

    print(f"Sum: {num1 + num2}")

    # break this out into a function to elimate repeated code
    num3 = prompt_num_input("Enter a number: ")
    num4 = prompt_num_input("Enter another number: ")

    print(f"Sum: {sum_numbers(num3,num4)}")


if __name__ == "__main__":
    main()
