# functions for my_events menu point
import file_functions
import functions
import ui
import main

TITLE_LIST_FOR_CREATE = ["ID", "Name", "Description","Place","Starting", "Ending", "Type"]

def start():
    while True:
        user_table = file_functions.read_from_file("Userinfo.csv", "user")
        options = ["Show events",
                   "Search",
                   "Create",
                   "Delete",
                   "Edit"]

        ui.print_menu("My Events Menu", options, "Exit to Main Menu")

        inputs = ui.get_inputs("Please enter a number:", "")
        option = inputs[0]
        if option == "1":
            show_events(main.email)
            pass
        elif option == "2":
            #functions.search()
            pass
        elif option == "3":
            create_event(file_functions.read_from_file("Eventinfo.csv", "event"), email)
            pass
        elif option == "4":
            #delete_event()
            pass
        elif option == "5":
            #table = edit_event(event_table, ui.get_inputs("Please give me an ID to update table element: ",
                                                #"Update line in table"))
            pass  
        elif option == "0":
            main.main()
        else:
            raise KeyError("There is no such option.")


def show_events(email):
    event_table = file_functions.read_from_file("Eventinfo.csv", "event")
    ui.print_result(functions.show_events_by_user(email, "my", event_table))

def create_event(file_table,user_email): # Andi
    table = file_table
    Id = functions.generate_random_eventID(table)
    new_list = []
    new_list.append(Id)
    while len(new_list) < len(TITLE_LIST_FOR_CREATE)-1:
        for title in TITLE_LIST_FOR_CREATE[1:]:
            new_list.append(ui.get_inputs("Give me {0}:".format(title), "Append database"))
    new_list.append(str(1231))
    new_list.append(str(user_email))
    table.append(new_list)
    print(new_list)
    file_functions.write_to_file("Eventinfo.csv", table)

def delete_event(): # Gabi
    pass


def edit_event(): # Tomi
    pass