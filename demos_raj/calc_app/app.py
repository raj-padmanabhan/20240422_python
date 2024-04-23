def main() -> None:
    result: float = 0.0
    # print(type(result))

    # infinite loop
    while True:
        # capture user input from teh command line
        command = input("Enter a command: ")

        if command == "exit":
            break
        elif command == "clear":
            result = 0.0

        operand_str = input("Please enter an operand: ")
        operand = float(operand_str)

        # https://docs.python.org/3/tutorial/controlflow.html#if-statements

        if command == "add":
            result += operand
        elif command == "subtract":
            result -= operand
        elif command == "multiply":
            result *= operand
        elif command == "divide":
            if operand != 0.0:
                result /= operand
        else:
            print("Invalid command. Please enter add\subtract\multiply\divide")

        print(f"Result:  {result}")
        # f-string is convenient way to format strings and evaluate variables in the string.
        # print(f"Received command:  {command}")
        # print(f"Received operand:  {operand}")


if __name__ == "__main__":
    main()
