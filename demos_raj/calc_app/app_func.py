from typing import Any


def get_operand_input() -> float:
    operand_str = input("Please enter an operand: ")
    return float(operand_str)


def record_command(id: int, commandstr: str, operand: str) -> dict:
    command: dict[str, Any] = {}
    command = {"id": id, "command": commandstr, "operand": operand}
    return command


def print_result(result: float) -> None:
    print(f"Result:  {result}")
    return


def remove_history(history: list) -> None:
    removeid = input("Please enter a history id: ")
    # print(f"Remove element {removeid}")
    for entry in history:
        if entry["id"] == int(removeid):
            print(history)
            history.remove(entry)
            print(history)
    return


def main() -> None:
    historyid = 1
    result: float = 0.0
    # print(type(result))

    # ERROR: history: list[dict[str, Any]] = {}
    history: list[dict[str, Any]] = []

    # infinite loop
    while True:
        # capture user input from teh command line
        command = input("Enter a command:")

        if command == "exit":
            break

        # https://docs.python.org/3/tutorial/controlflow.html#if-statements

        if command == "add":
            operand = get_operand_input()
            history.append(record_command(historyid, command, operand))
            historyid += 1
            result += operand
            print_result(result)
        elif command == "subtract":
            operand = get_operand_input()
            history.append(record_command(historyid, command, operand))
            historyid += 1
            result -= operand
            print_result(result)
        elif command == "multiply":
            operand = get_operand_input()
            history.append(record_command(historyid, command, operand))
            historyid += 1
            result *= operand
            print_result(result)
        elif command == "divide":
            operand = get_operand_input()
            history.append(record_command(historyid, command, operand))
            historyid += 1
            if operand != 0.0:
                result /= operand
            print_result(result)
        elif command == "history":
            print(history)
        elif command == "remove":
            remove_history(history)
        elif command == "clear":
            result = 0.0
        else:
            print("Invalid command.")
            print("Please enter add\subtract\multiply\divide\history")

        # f-string is convenient way to format strings and evaluate
        # variables in the string.
        # print(f"Received command:  {command}")
        # print(f"Received operand:  {operand}")


if __name__ == "__main__":
    main()
