# main py file for the app.
# contains menu structure
import sys
import os
import ui
import my_events
import join_events
import functions
import file_functions


# list of menu points:
# if a menupoint was choosen -> run the adequate function from functions.py


def starting_screen():
    inputs = ui.get_inputs("Please enter a number: ", "")
    option = inputs[0]
    if option == "1":
        functions.user_reg()
    elif option == "2":
        user_database = file_functions.read_from_file("Userinfo.csv", "user")
        email = functions.user_login(user_database)
        return email
    elif option == "3":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def choose_menupoint():
    inputs = ui.get_inputs("Please enter a number: ", "")
    option = inputs[0]
    if option == "1":
        my_events.start()
    elif option == "2":
        join_events.start()
    elif option == "3":
        functions.search()
    elif option == "4":
        functions.show_random_events()
    elif option == "5":
        functions.join_event()
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def starting_screen_optionlist():
    options = ["Register new account",
               "Login with existing account"]
    ui.print_menu("Welcome to EventApp", options, "Exit program")


# list of strings, for menu print in ui.py
def menu_optionlist():
    options = ["Show created events",
               "Show events I joined",
               "Search Event",
               "Show new random events",
               "Join Event"]
    ui.print_menu("Main menu", options, "Exit program")


# menu structure in a while loop until user quit
def main():
    email = ""
    while email is "":
        starting_screen_optionlist()
        try:
            email = starting_screen()
            print(email)
        except KeyError as err:
            ui.print_error_message(err)
    while True:
        menu_optionlist()
        try:
            choose_menupoint()
        except KeyError as err:
            ui.print_error_message(err)


if __name__ == '__main__':
    main()
