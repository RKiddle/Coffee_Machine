
def normalize(name):
    my_table = name.maketrans("éëáå", "eeaa")
    new_name = name.translate(my_table)
    new_name = new_name.replace("œ", "oe")
    new_name = new_name.replace("æ", "ae")

    return new_name

print(normalize(name))
