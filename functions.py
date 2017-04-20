# input and print functions.
# functions to get or change datga in files
import ui
import file_functions
CREATOR_INDEX = 8
PARTICIPANT_INDEX = 7

# e-mail, name, password
def user_reg(database): # Peti
    pass


# e-mail, password, return with e-mail
def user_login(database): # Peti
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


def show_events_by_user(email, show_type, database):
    #find events in database by email
    #return new event list
    temp = database
    user_database = []
    if show_type == "join":
        for item in temp:
            if email in item[PARTICIPANT_INDEX]:
                user_database.append(item)
        return user_database
    elif show_type == "my":
        for item in temp:
            if email in item[CREATOR_INDEX]:
                user_database.append(item)
        return user_database



def show_random_events(database): # Gabi
    pass


def search(paramater, database): # Andi
    #search in database by paramater
    #return new event list
    pass


def join_event(data): # White
    #join event by ID
    pass