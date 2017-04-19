# functions for joiined events


def start():
    while True:
        event_table = file_functions.read_from_file("Eventinfo.csv")
        user_table = file_functions.read_from_file("Userinfo.csv")
        #functions.show_events(email, event_table)

        options = ["Search",
                   "Create",
                   "Delete",
                   "Edit"]

        ui.print_menu("My Events Menu", options, "Exit to Main Menu")

        inputs = ui.get_inputs("Please enter a number:", "")
        option = inputs[0]
        if option == "1":
            #functions.search()
            pass
        elif option == "2":
            #event_table = create_event
            pass
        elif option == "3":
            #delete_event()
            pass
        elif option == "4":
            #table = edit_event(event_table, ui.get_inputs("Please give me an ID to update table element: ",
                                                #"Update line in table"))
            pass  
        elif option == "0":
            main.main()
        else:
            raise KeyError("There is no such option.")


def quit_event(data):
    pass