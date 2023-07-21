def BiggerGreater(instr: str) -> str:

    if instr == "".join(sorted(instr, reverse=True)):
        return ""

    for i in range(len(instr)-2, -1, -1):
        if instr[i:] == "".join(sorted(instr[i:], reverse=True)):
            continue

        index_ = sorted(instr[i:]).index(instr[i])+1
        remain = "".join(sorted(instr[i:]))

        return instr[:i] + remain[index_] + remain[:index_] + remain[index_+1:]
