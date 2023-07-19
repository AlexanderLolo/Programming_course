current_string = ""
all_states = []
position = -1
state = False


def BastShoe(command: str) -> str:

    if command[0] == "1":
        return Add(command[2:])

    if command[0] == "2":
        return Delete(int(command[2:]))

    if command[0] == "3":
        return Give(int(command[2:]))

    if command[0] == "4":
        return Undo()

    if command[0] == "5":
        return Redo()


def Add(add: str) -> str:

    global current_string
    global all_states
    global position
    global state

    if state:
        all_states = [current_string]
        position = 0
        state = False

    current_string += add
    all_states.append(current_string)
    position += 1

    return current_string


def Delete(N: int) -> str:

    global current_string
    global all_states
    global position
    global state

    if state:
        all_states = [current_string]
        position = 0
        state = False

    current_string = current_string[:-N]
    all_states.append(current_string)
    position += 1

    return current_string


def Give(N: int) -> str:

    global current_string

    return current_string[N:N+1]


def Undo() -> str:

    global position
    global state
    global current_string

    state = True

    if position == 0:
        return current_string
    
    position -= 1
    current_string = all_states[position]
    return all_states[position]


def Redo() -> str:

    global position
    global state
    global current_string

    state = True
    if position == len(all_states)-1:
        return current_string

    position += 1
    current_string = all_states[position]
    return all_states[position]
