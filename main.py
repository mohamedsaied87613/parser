from Compiler import Compiler


def main():

    # Get the input from the user
    statement = input("Enter an assignment statement: ")

    try:
        # Call the tokenizer function to check the assignment statement
        compiler=Compiler(statement)
        print(compiler.parsed_statement)

        # If the function returns without raising an exception, the assignment statement is valid
        print("Assignment statement is valid:", statement)


    except ValueError as e:
        # If the function raises a ValueError exception, the assignment statement is invalid
        print("Assignment statement is invalid:", statement)
        # Print the error message
        print(e)
        pass

# Call the main function
if __name__ == "__main__":
    main()
