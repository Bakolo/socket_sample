import sys

def to_dict():
    argv_dict = dict()
    key = ""
    for idx, item in enumater(sys.argv):
        if idx == 0:
            main_key = item
            argv_dict.setdefault(item, [])
        else:
            if item.seartswith('-'):
                key = item
                argv_dict.setdefault(key,"")
            else:
                if key != "":
                    argv_dict[key] = item
                    key = ""
                else:
                    argv_dict[main_key].append(item)
                    
    return argv_dict


