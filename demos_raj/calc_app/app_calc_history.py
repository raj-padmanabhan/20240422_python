from typing import Any

def main() -> None:
    historyid = 1
    result: float = 0.0
    # print(type(result))

    # ERROR: history: list[dict[str, Any]] = {}
    history: list[dict[str, Any]] = []

    # infinite loop
    while True:
        # capture user input from teh command line
        command = input("Enter a command: ")

        if command == "exit":
            break
        elif command == "clear":
            result = 0.0

        # https://docs.python.org/3/tutorial/controlflow.html#if-statements

        if command == "add":
            operand_str = input("Please enter an operand: ")
            operand = float(operand_str)
            history.append(
                {"id": historyid, "command": command, "operand": operand}
            )
            historyid += 1
            result += operand
        elif command == "subtract":
            operand_str = input("Please enter an operand: ")
            operand = float(operand_str)
            history.append(
                {"id": historyid, "command": command, "operand": operand}
            )
            historyid += 1
            result -= operand
        elif command == "multiply":
            operand_str = input("Please enter an operand: ")
            operand = float(operand_str)
            history.append(
                {"id": historyid, "command": command, "operand": operand}
            )
            historyid += 1
            result *= operand
        elif command == "divide":
            operand_str = input("Please enter an operand: ")
            operand = float(operand_str)
            history.append(
                {"id": historyid, "command": command, "operand": operand}
            )
            historyid += 1
            if operand != 0.0:
                result /= operand
        elif command == "history":
            print(history)
        elif command == "remove":
            removeid = input("Please enter a history id: ")
            # print(f"Remove element {removeid}")
            for entry in history:
                if entry["id"] == int(removeid):
                    print(history)
                    history.remove(entry)
                    print(history)
        else:
            print("Invalid command.")
            print("Please enter add\subtract\multiply\divide\history")

        print(f"Result:  {result}")
        # f-string is convenient way to format strings and evaluate
        # variables in the string.
        # print(f"Received command:  {command}")
        # print(f"Received operand:  {operand}")


if __name__ == "__main__":
    main()
