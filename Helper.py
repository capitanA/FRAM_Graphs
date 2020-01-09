def edge_detector(aspect_in):
    i = False
    p = False
    t = False
    c = False
    r = False

    if aspect_in == "I":
        i = True
    elif aspect_in == "P":
        p = True
    elif aspect_in == "T":
        t = True
    elif aspect_in == "C":
        c = True
    elif aspect_in == "R":
        r = True
    return i, p, t, c, r


def check_which_aspect(aspect):
    # pdb.set_trace()
    # print(type(aspect))
    if aspect.isnumeric():
        # if isinstance(aspect,int):
        if aspect == "1":
            return "C"
        elif aspect == "2":
            return "T"
        elif aspect == "3":
            return "I"
        elif aspect == "4":
            return "P"
        elif aspect == "5":
            return "R"
        elif aspect == "6":
            return "O"
    else:
        return aspect
