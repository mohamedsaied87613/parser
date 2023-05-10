class Compiler:
    def __init__(self, statement):
        self.statement = statement

        # Define a list of allowed characters in an assignment statement
        self.acceptableChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789=+-*/%()"
        self.operator = "=+-*/%()"

        stack = self.tokenizer()
        self.parsed_statement = self.Parser(stack)

    def tokenizer(self):
        # Create an empty stack
        stack = []

        # Create an empty set to store = char in it and anything should be occurred one time only
        seen_chars = set()

        # Loop through each character in the assignment statement
        for char in self.statement:
            # condition to make sure that the statement is assignment statement
            if self.statement[1] != '=':
                raise ValueError("Illegal character in assignment statement: {}".format(char))

            # to check if two operators come in successive
            if char in self.operator and stack[-1] in self.operator:
                raise ValueError("Illegal character in assignment statement: {}".format(char))

            # Check if the character is accepted
            if char in self.acceptableChars:
                # If the character is accepted, push it onto the stack
                stack.append(char)
                seen_chars.add(char)
            else:
                # If the character is not accepted, raise an exception
                raise ValueError("Illegal character in assignment statement: {}".format(char))

        # Return the stack
        return stack

    def Parser(self, stack):
        operations = ""
        variables = ""
        # =+-*/%()
        translator = {"*": "MUL", "+": "ADD", "-": "MIN", "/": "DIV", "%": "MOD", "(": "OPEN", ")": "CLOSE"
            , "CHAR": ["LIT", "LOAD"], "digit": "LIT", "=": "STORE"}

        # print("ops", operations)
        # print("vars", variables)
        while stack:
            element = stack.pop()

            if self.operator.find(element) != -1:
                operations = operations + translator.get(element) + ' '

            elif element.isdigit():
                variables = translator.get('digit') +' '+ element + ' '+variables

            else:
                variables = translator.get('CHAR')[0] + ' ' + element + ' ' + translator.get('CHAR')[
                    1] + ' ' + variables

        variables = variables.replace("LOAD", "", 1)
        variables=variables.replace("  ", " ")
        return variables + operations
