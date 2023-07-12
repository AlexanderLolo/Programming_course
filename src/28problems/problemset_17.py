def LineAnalysis(line: str) -> bool:

    if line == "*":
        return True

    splitted = line.split("*")[1:-1]
    return len(max(splitted)) == len(min(splitted))
