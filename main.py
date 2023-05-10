# Define the tokenizer function
def tokenizer(statement):
    # Create an empty stack
    stack = []

    # Define a list of allowed characters in an assignment statement
    acceptableChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789=+-*/%()"
    operator        = "=+-*/%()"

    # Create an empty set to store = char in it and any thing should be occur one time only
    seen_chars = set()

    # Loop through each character in the assignment statement
    for char in statement:
        # condition to make sure that the statement is assignment statement
        if statement[1] != '=':
            raise ValueError("Illegal character in assignment statement: {}".format(char))

        # to check if two operators come in successive
        if char in operator and stack[-1] in operator:
            raise ValueError("Illegal character in assignment statement: {}".format(char))

        # Check if the character is accepted
        if char in acceptableChars:
            # If the character is accepted, push it onto the stack
            stack.append(char)
            seen_chars.add(char)
        else:
            # If the character is not accepted, raise an exception
            raise ValueError("Illegal character in assignment statement: {}".format(char))

    # Return the stack
    return stack


# Define the main function
def main():

    # Get the input from the user
    statement = input("Enter an assignment statement: ")

    try:
        # Call the tokenizer function to check the assignment statement
        stack = tokenizer(statement)

        # If the function returns without raising an exception, the assignment statement is valid
        print("Assignment statement is valid:", statement)

        # Print the contents of the stack
        print("Stack contents:", stack)

    except ValueError as e:
        # If the function raises a ValueError exception, the assignment statement is invalid
        print("Assignment statement is invalid:", statement)
        # Print the error message
        print(e)


# Call the main function
if __name__ == "__main__":
    main()
