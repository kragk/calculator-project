## Simple Two Number Calculator

## Calculation Function
def calculation(first_number, second_number, calc_type):
    if(calc_type == "+"):
        print(first_number+second_number)
    elif(calc_type == "-"):
        print(first_number-second_number)
    elif(calc_type == "x"):
        print(first_number*second_number)
    elif(calc_type == "/"):
        print(first_number/second_number)
    else:
        print("Not a valid calculation.")
    return


## Establishing the Numbers
first_number = int(input("First Number: "))
second_number = int(input("Second Number: "))


## Calculation Type
calculations = input("Calculation Type: ")

## Print Function
calculation(first_number,second_number,calculations)