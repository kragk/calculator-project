# more complex calculator...

# global variables
calculation_sequence = []
user_input = ""


while user_input != "done":
    temp_index = 0

    # the input function is a STRING!
    user_input = input("Input operator or number: ")

    # is the user done inputting?
    if user_input.lower() == 'done':
        break

    # user_input is an operator AND calculation_sequence[index - 1] is a number, then, continue
    elif user_input in ["+", "-", "/", "*"] and isinstance(calculation_sequence[temp_index - 1], (float,int)):
        calculation_sequence.append(user_input)

    # user_input is a number AND calculation_sequence[index - 1] is a number, then, error!

    # previous was operator, cant have TWO operators in a row
    #
    # DEBUG! INDEX - 1 ONLY WORKS WHEN INDEX > 0
    elif user_input in ["+", "-", "/", "*"] and calculation_sequence[temp_index - 1] in ["+", "-", "/", "*"]:
        try:
            print("Previous was an operator. Enter a number.")
        except IndexError:
            pass

    # is it a number?
    else:

        # it IS a number
        try:

            # IF it works, then check if calculation_sequence[index - 1] is a number.
            number = float(user_input)


        # it is NOT a number
        except ValueError:
            print("Not a number or operator")
            continue

    # checks if previous iteration was a number and therefore cannot enter number now
    try:
        if isinstance(calculation_sequence[temp_index - 1], (float,int)) and isinstance(number,(float,int)):
            print("You previously entered a number, enter an operator.")
    except IndexError:
        pass

    else:
        calculation_sequence.append(number)

    # index for seeing if there is two operators or two numbers IN A ROW
    temp_index = temp_index + 1

print(calculation_sequence)

for i in range(len(calculation_sequence)):
    item = calculation_sequence[i]
