# input and print functions for ui.
import os

# chechking user inputs (type, etc.)
def get_inputs(list_labels, title):
    inputs = input(list_labels)
    while not inputs:
        inputs = input(list_labels)
    return inputs


# menu formating
def print_menu(title, list_options, exit_message):
    print(title)
    for index, option in enumerate(list_options):
        print("({0}) {1}".format(index + 1, option))
    print("(0) {0}".format(exit_message))


# error message if inputs are not correct or something goes wrong
def print_error_message(message):
    print(message)


# for example: print result of search or list of events created by the user, etc.
def print_result(table, title_list=["ID", "Name", "Description","Place","Starting", "Ending", "Type", "Participants", "Creator"]):
    os.system('clear')
    columns_max_length = [0] * len(title_list)
    counter = 0
    for i in table:
        table[counter][title_list.index("Participants")] = str(len(table[counter][title_list.index("Participants")]))
        counter += 1
    table.insert(0, title_list)
    for row in table:
        counter_columns = 0
        while counter_columns <= len(row) - 1:
            if len(row[counter_columns]) > columns_max_length[counter_columns]:
                if len(row[counter_columns]) % 2 != 0:
                    columns_max_length[counter_columns] = int(len(row[counter_columns]) + 1)
                else:
                    columns_max_length[counter_columns] = int(len(row[counter_columns]))
            counter_columns += 1
    table_lenght = 0
    for lenghts in columns_max_length:
        table_lenght = table_lenght + lenghts
    for row in table:
        print("-" * (table_lenght + len(columns_max_length) + 1))
        counter_columns = 0
        while counter_columns <= len(row) - 1:
            space = " " * (columns_max_length[counter_columns] - len(row[counter_columns]))
            print("|", space, row[counter_columns], end="", sep="")
            counter_columns += 1
        print("|")
    print("-" * (table_lenght + len(columns_max_length) + 1))
    del table[0]



