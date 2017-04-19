# input and print functions for ui.


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
def print_result(result, label):
    print(label, '\n', result)



