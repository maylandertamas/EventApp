# functions for my_events menu point
import file_functions
import functions
import ui
import main

TITLE_LIST_FOR_CREATE = ["ID", "Name", "Description","Place","Starting", "Ending", "Type", "Creator"]

def start():
    while True:
        event_table = file_functions.read_from_file("Eventinfo.csv", "event")
        user_table = file_functions.read_from_file("Userinfo.csv", "user")
        ui.print_result(functions.show_events_by_user("test@test.com", "my", event_table))
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


def create_event(): # Andi
    Id = functions.generate_random_eventID(file_functions.read_from_file)
    new_list = []
    new_list.append(Id)
    while len(new_list) < len(TITLE_LIST_FOR_CREATE)-1:
        for title in TITLE_LIST_FOR_CREATE:
            new_list.append(ui.get_inputs("Give me {0}:".format(title)))
    new_list.insert(7, "")
    #file_functions.write_to_file("Eventinfo.csv", new_list)

def delete_event(): # Gabi
    pass


def edit_event(): # Tomi
    pass