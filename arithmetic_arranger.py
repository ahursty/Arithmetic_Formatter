import re


def arithmetic_arranger(problems, solve=False):
    # this:
    # ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

    # into this:
    #      32      3801      45      123
    #   + 698    -    2    + 43    +  49
    #   -----    ------    ----    -----

    # errors to check:
    # too many problems, must be 5 or less with error message "Error: Too many problems."
    # addition and subtraction only, multiplication & division will return error message "Error: Operator must be '+' or '-'."
    # digits only, otherwise return error "Error: Numbers bust only contain digits."
    # max 4 digits in width, otherwise returns error "Error: Numbers cannot be more than four figits."

    if (len(problems) > 5):
        return "Error: Too many problems."

    first = ""
    second = ""
    lines = ""
    sumx = ""
    string = ""

    for problem in problems:
        if (re.search("[^\s\d.+-]", problem)):
            if (re.search("[/]", problem) or re.search("[*]", problem)):
                return "Error: Operator must be '+' or '-'."
            return "Error: Number must only contain digits."

        # split strings by each space, then assign to variable based on index
        first_number = problem.split(" ")[0]
        operator = problem.split(" ")[1]
        second_number = problem.split(" ")[2]

        if (len(first_number) >= 5 or len(second_number) >= 5):
            return "Error: Numbers cannot be more than four digits."

        sum = ""

        if (operator == '+'):
            sum = str(int(first_number) + int(second_number))
        elif (operator == '-'):
            sum = str(int(first_number) - int(second_number))

        # Get max length between operands, will be a number 1-4
        length = max(len(first_number), len(second_number)) + 2
        # Top of output string will be 1st number right-adjusted by value of length (1-4)
        top = str(first_number).rjust(length)
        bottom = operator + str(second_number).rjust(length - 1)
        line = ""

        res = str(sum).rjust(length)
        for s in range(length):
            line += "-"

        if problem != problems[-1]:
            first += top + '    '
            second += bottom + '    '
            lines += line + '    '
            sumx += res + '    '
        else:
            first += top
            second += bottom
            lines += line
            sumx += res

    if solve:
        string = first + "\n" + second + "\n" + lines + "\n" + sumx
    else:
        string = first + "\n" + second + "\n" + lines
    return string