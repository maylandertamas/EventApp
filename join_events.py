# functions for joiined events


def start():
    while True:
        event_table = file_functions.read_from_file("Eventinfo.csv")
        user_table = file_functions.read_from_file("Userinfo.csv")
        #functions.show_events(email, event_table)

        options = ["Search",
                   "Quit event"]

        ui.print_menu("Joined Event's Menu", options, "Exit to Main Menu")

        inputs = ui.get_inputs("Please enter a number:", "")
        option = inputs[0]
        if option == "1":
            #functions.search()
            pass
        elif option == "2":
            #quit_event()
            pass  
        elif option == "0":
            main.main()
        else:
            raise KeyError("There is no such option.")


def quit_event(data): # White
    pass