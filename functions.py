# input and print functions.
# functions to get or change datga in files
import ui
import file_functions
import random
from datetime import datetime

CREATOR_INDEX = 8
PARTICIPANT_INDEX = 7

# e-mail, name, password
def user_reg(database):
    pass


# e-mail, password, return with e-mail
def user_login(database):
    print(database)
    E_MAIL_INDEX = 0
    PASSWORD_INDEX = 2
    email = ui.get_inputs("Please enter your e-mail adress: ", "")
    print(email)
    password = ui.get_inputs("Please enter your password: ", "")
    print(password)
    for i in range(len(database)):
        if database[i][E_MAIL_INDEX] == email:
            for i in range(len(database)):
                if database[i][PASSWORD_INDEX] == password:
                    print("Succesfully logged in.")
                    return email
    print("Wrong e-mail adress, or password.")


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



def show_random_events(): # Gabi 2017-09-16-5:00
    temp_event_list = []
    events = file_functions.read_from_file("Eventinfo.csv")
    present = datetime.now()
    #datetime_object = datetime.strptime(events[0][5], '%Y-%m-%d-%H:%M')
    for i in range(4):
        temp_event = random.choice(events)
        if temp_event not in temp_event_list and present < str_to_date(temp_event[5]):
            temp_event_list.append(temp_event)
    ui.print_result(temp_event_list)


def search(paramater, database): # Andi
    #search in database by paramater
    #return new event list
    pass


def join_event(data): # White
    #join event by ID
    pass


def str_to_date(string):
    return datetime.strptime(string, '%Y-%m-%d-%H:%M')
