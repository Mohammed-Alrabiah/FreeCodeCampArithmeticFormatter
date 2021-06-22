def arithmetic_arranger(strlst, ansr = None):

    first_nums_lst = []
    second_nums_lst = []
    operators_lst = []
    first_row = ""
    second_row = ""
    third_row = ""
    fourth_row = ""
    i = 0
    if len(strlst) > 5:
        print("Error: Too many problems.")
        quit()

    for j in strlst:
        com = j.split()
        first_nums_lst.append(com[0])
        second_nums_lst.append(com[2])
        operators_lst.append(com[1])

    while i < len(first_nums_lst):
        if operators_lst[i] != "+":
            if operators_lst[i] != "-":
                print("Error: Operator must be '+' or '-'.")
                quit()
        try:
            int(first_nums_lst[i])
            int(second_nums_lst[i])
        except:
            print("Error: Numbers must only contain digits.")
            quit()
        if len(first_nums_lst[i]) > 4 or len(second_nums_lst[i]) > 4:
            print("Error: Numbers cannot be more than four digits.")
            quit()

        if operators_lst[i] == "+":
            total = int(first_nums_lst[i]) + int(second_nums_lst[i])
        else:
            total = int(first_nums_lst[i]) - int(second_nums_lst[i])

        if len(first_nums_lst[i]) >= len(second_nums_lst[i]):
            first_row = first_row + "  " + (first_nums_lst[i]) + "    "
            second_row = second_row + operators_lst[i] + " " + ((len(first_nums_lst[i]) - len(second_nums_lst[i])) * " ") + second_nums_lst[i] + "    "
            third_row = third_row + "--" + ("-" * len(first_nums_lst[i])) + "    "
            a = "--" + ("-" * len(first_nums_lst[i]))
            fourth_row = fourth_row + (" " * (len(a) - len(str(total)))) + str(total) + "    "
        else:
            first_row = first_row + "  " + ((len(second_nums_lst[i]) - len(first_nums_lst[i])) * " ") + first_nums_lst[i] + "    "
            second_row = second_row + operators_lst[i] + " " + second_nums_lst[i] + "    "
            third_row = third_row + "--" + ("-" * len(second_nums_lst[i])) + "    "
            a = "--" + ("-" * len(second_nums_lst[i]))
            fourth_row = fourth_row + (" " * (len(a) - len(str(total)))) + str(total) + "    "
        i = i+1

    fr = first_row.rstrip()
    sr = second_row.rstrip()
    tr = third_row.rstrip()
    fth = fourth_row.rstrip()
    if ansr == True:
        return fr + "\n" + sr + "\n" + tr + "\n" + fth
    else:
        return fr + "\n" + sr + "\n" + tr


print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40"], True))
