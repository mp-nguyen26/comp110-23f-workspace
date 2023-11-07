"""Writing functions involving dictionaries."""

__author__ = "730574011"

def invert(inp_dict: dict[str,str]) -> dict[str,str]:
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
    list_of_colors = []
    for keys in inp_dict:
        list_of_colors.append(inp_dict[keys])
    for colors in list_of_colors





