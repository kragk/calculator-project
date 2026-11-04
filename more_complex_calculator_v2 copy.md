# more_complex_calculator_v2

# estabilish global var
from turtle import done


calculation_sequence = []
user_input = ""

# what functions are needed?

# check if user is done inputting
def done_input():
    if(user_input == "done"):
        return True
    else:
        return False

# check if last iteration of calculation_sequence was a number, and did user input a number this iteration?

def check_number(index):
    temp_input = user_input
    try:

        # try converting the string into a float to see if is a number or not
        temp_input = float(temp_input)

    except ValueError:

        # user did not input a number this current iteration.
        return False

    try:
        temp_input = float(calculation_sequence[index - 1])

    except IndexError:
        return False

    except ValueError:
        return False

    return True

# check operators
# 1. is this the first input? if it is, there cannot be an operator (ex. [+,1,+, it makes no sense) (if yes)--> false
# 2. is last iteration of calculation_sequence an operator? AND is current iteration an operator (if yes) --> false
# 3. return true
def check_operators(index):
    if not index > 0:
        return False
    elif calculation_sequence[index - 1] in ["+", "-", "/", "*"] and user_input in ["+", "-", "/", "*"]:
        return False
    else:
        return True


# main loop
index = 0
while done_input is False:
    user_input = input("Input an operator or number: ")
    done_input()
    if done_input():
        break

    elif check_operators(index) is False:
        print("You cant enter an operator. Enter a number.")
        continue

    elif check_number(index) is False:
        print("You cant enter a number. Enter an operator.")
        continue

    elif check_number(index) is True:
        calculation_sequence.append(float(user_input))

    elif check_operators(index) is True:
        calculation_sequence.append(user_input)

    print(calculation_sequence)
    index = index + 1
