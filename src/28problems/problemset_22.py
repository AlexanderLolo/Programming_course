def SherlockValidString(instr: str) -> bool:

    dict1 = {i: instr.count(i) for i in set(instr)}
    set_ = set(dict1.values())

    return (len(set_) == 1 or
            len(set_) == 2 and abs(list(set_)[0] - list(set_)[1]) == 1 and
            min(list(dict1.values()).count(list(set_)[0]),
                list(dict1.values()).count(list(set_)[1])) == 1)
