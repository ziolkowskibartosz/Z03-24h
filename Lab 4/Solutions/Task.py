valid_char = True

def is_expression_valid(expression):
    for char in expression:
        if not char in valid_chars:
            return not valid_char
    return valid_char   

valid_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '+', '-', '/', '*', '.', '(', ')']
                    






expression = input("Type an expression you want to count: ")

if is_expression_valid(expression):
    try:
        print(str(expression) + " = " + str(eval(expression)))
    except:
        print("Something went wrong")
else:
    print("The expression consists of invalid chars")
