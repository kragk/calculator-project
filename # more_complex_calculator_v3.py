# more_complex_calculator_v3

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


user_input = 0
calc_seq = []
while str(user_input).lower() != 'done':
    print(calc_seq)
    user_input = input("Input a number or an operator. Input DONE if finished: ")
    if user_input == 'done':
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
