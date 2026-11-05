# more_complex_calculator_v3

# functions
def number_check(input):

    try:
        input = float(input)
        return True

    except ValueError:
        return False

def operator_check(input):
    if input in ['+', '-', '*', '/']:
        return True
    else:
        return False

# ---------------------------------------------------------------------------------------------

user_input = 0
calc_seq = []

# COMPLETE. NO NEED FIX.
while str(user_input).lower() != 'done':
    print(calc_seq)
    user_input = input("Input a number or an operator. Input DONE if finished: ")
    if str(user_input).lower() == 'done':
        if len(calc_seq) == 0:
            print("Enter at least one number.")
        elif operator_check(calc_seq[-1]):
            print("Cannot end on an operator.")
        else:
            print("Calculating...")
            break

    elif len(calc_seq) == 0 and number_check(user_input):
        calc_seq.append(float(user_input))
    elif len(calc_seq) == 0 and number_check(user_input) is False:
        print('Enter a number. Not an operator for the first.')

    elif operator_check(user_input) and number_check(calc_seq[-1]):
        calc_seq.append(user_input)
        print('Success')

    elif operator_check(calc_seq[-1]) and number_check(user_input):
        calc_seq.append(float(user_input))
        print('Success')

    elif number_check(user_input) and number_check(calc_seq[-1]):
        print('Cannot enter two numbers in a row.')
    else:
        print("Cant enter two operators in a row.")

# reading and calculation
total = calc_seq[0]

for index, calc_seq_present in enumerate(calc_seq):
    if index > len(calc_seq) - 2:
        break
    elif number_check(calc_seq_present):
        if calc_seq[index + 1] == '+':
            total = total + calc_seq[index + 2]
        elif calc_seq[index + 1] == '-':
            total = total - calc_seq[index + 2]
        elif calc_seq[index + 1] == '/':
            total = total / calc_seq[index + 2]
        elif calc_seq[index + 1] == '*':
            total = total * calc_seq[index + 2]

print("Answer: ", total)
