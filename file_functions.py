# Tomi

# functions to read or write datas in file

# write new lines or change datas in the file
def write_to_file(file_name, table):
    with open(file_name, "w") as file:
        for record in table:
            row = ';'.join(record)
            file.write(row + "\n")


# maybe make a list from the datas in file?
def read_from_file(file_name, file_type):
    with open(file_name, "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(";") for element in lines]
    if file_type == "event":
        for item in table:
            item[7] = item[7].split(',')
        return table
    elif file_type == "user":
        return table
