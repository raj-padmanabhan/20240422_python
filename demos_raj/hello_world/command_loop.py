def main() -> None:
    # infinite loop
    while True:
        # capture user input from teh command line
        command = input("Enter a command: ")

        if command == "exit":
            break

        # f-string is convenient way to format strings and evaluate variables in the string.
        print(f"Received command:  {command}")


if __name__ == "__main__":
    main()
