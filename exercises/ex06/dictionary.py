"""Writing functions involving dictionaries."""

__author__ = "730574011"

def invert(inp_dict: dict[str,str]) -> dict[str,str]:
    """Given a dictionary of strings, returns a dictionary where keys and values are swapped."""
    new_dict = {}
    list_of_keys = []
    list_of_values = []
    for keys in inp_dict:
        list_of_keys.append(keys)
        # new_dict[keys] = keys
        list_of_values.append(inp_dict[keys])
        for elem in list_of_values:
            #  new_dict.pop(elem)
             for idx in range(0, len(list_of_keys)):
                new_dict[list_of_values[idx]] = list_of_keys[idx]
    if len(new_dict) == len(list_of_keys):
        return new_dict
    else:
        raise KeyError("Womp Womp...The resulting dictionary has duplicate key(s)!")
    

def favorite_color(inp_dict: dict[str,str]) -> str:
    """Given a dictionary of strings, returns the most popular color value."""
    color_count: dict[str,int] = {}
    for keys in inp_dict:
        if inp_dict[keys] in color_count:
            color_count[inp_dict[keys]] += 1
        else:
            color_count[inp_dict[keys]] = 1
    popular_color: str = ""
    count: int = 0
    for color in color_count:
        if color_count[color] > count:
            popular_color = color
            count = color_count[color]
    return popular_color


def count(inp_list: list[str]) -> dict[str,int]:
    """Given a list of strings, returns a dictionary that has each string and its frequency."""
    freuency_dict: dict[str,int] = {}
    for strings in inp_list:
        if strings in freuency_dict:
            freuency_dict[strings] += 1
        else:
            freuency_dict[strings] = 1
    return freuency_dict


def alphabetizer(inp_list: list[str]) -> dict[str,list[str]]:
    """Given a list of strings, returns a dictionary with each first letter, and the words that start with that letter."""
    result_dict: dict[str,list[str]] = {}
    for strings in inp_list:
        if strings[0].lower() in result_dict:
            result_dict[strings[0]].append(strings)
        else:
            result_dict[strings[0].lower()] = []
            result_dict[strings[0].lower()].append(strings)
    return result_dict


def update_attendance(inp_dict: dict[str,list[str]], day: str, student: str) -> dict[str,list[str]]:
    """Gievn a dictionary of days of the week and students present, mutates that dictionary with new stuents and days."""
    if day in inp_dict and student not in inp_dict[day]:
        inp_dict[day].append(student)
    else:
        inp_dict[day] = student
    return inp_dict





