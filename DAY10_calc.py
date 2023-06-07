print()

from import_function import clear_screen
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
clear_screen()
print (logo)
print()

#FUNCTION : performs operations based on user input (operation)
def operatons(operation,num1,num2):
    if operation=='+':
        return num1+num2
    elif operation=='-':
        return num1-num2
    elif operation=='*':
        return num1*num2
    elif operation=='/':
        return num1/num2
    else :
        return 'Invalid operation entered'

continue_ = True

while continue_:
    num1 = float(input("Enter number 1 : "))
    true_continue = True
    while true_continue:
        operation = input("Which operation \n+  \n-  \n*  \n/\n")
        num2 = float(input("Enter number 2 : "))
        if operation == '+':
            result = operatons(operation,num1,num2)
        elif operation=='-':
            result = operatons(operation,num1,num2)
        elif operation=='*':
            result = operatons(operation,num1,num2)
        elif operation=='/':
            result = operatons(operation,num1,num2)

        print(f"{num1} {operation} {num2} = {result}\n")

        wish_to_continue = True 
        while wish_to_continue:
            ask = input(f"Type 'y' to continue with {result}, or 'n' to start a new calculation : ").lower()
            if ask=='y':
                num1 = result
                wish_to_continue = False
            elif ask=='n':
                clear_screen()
                wish_to_continue = False
                true_continue = False
                break
            exit_ans = input("Do u want to exit the session ? (y/n) : ").lower()
            if exit_ans=='y':
                clear_screen()
                continue_ = False
            elif exit_ans=='n':
                clear_screen()
                wish_to_continue = False
                true_continue = False
                break


