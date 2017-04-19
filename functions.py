# input and print functions.
# functions to get or change datga in files
import ui
import file_functions


# e-mail, name, password
def user_reg(database):
    pass


# e-mail, password, return with e-mail
def user_login(database):
    pass


def generate_random_eventID(database):
    lower_case_chars = string.ascii_lowercase
    numbers = "0123456789"
    generated = ''
    generated_list = list(generated)
    generated_list = [random.choice(lower_case_chars), "H", random.choice(numbers),
                      random.choice(numbers), "J", random.choice(lower_case_chars), "#&"]
    generated = "".join(generated_list)

    while generated in table:
        generate_random(table)
    else:
        return generated


def show_events(id, database):
    #find events in database by id
    #return new event list
    pass


def show_random_events(database):
    pass


def search(paramater, database):
    #search in database by paramater
    #return new event list
    pass


def join_event(data):
    #join event by ID
    pass