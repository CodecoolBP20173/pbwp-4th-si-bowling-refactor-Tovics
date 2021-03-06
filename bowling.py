
def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for i in range(len(game)):
        if game[i] == '/':
            result += get_value(game[i]) - last
        else:
            result += get_value(game[i])
        if frame < 10 and get_value(game[i]) == 10:
            if game[i] == '/':
                result += get_value(game[i + 1])
            elif game[i] in 'Xx':
                result += get_value(game[i + 1])
                if game[i + 2] == '/':
                    result += get_value(game[i]) - get_value(game[i + 1])
                else:
                    result += get_value(game[i + 2])
        last = get_value(game[i])
        if not in_first_half:
            frame += 1
        if in_first_half is True:
            in_first_half = False
        else:
            in_first_half = True
        if game[i] == 'X' or game[i] == 'x':
            in_first_half = True
            frame += 1
    return result


def get_value(char):
    if char in '123456789':
        return int(char)
    elif char in 'Xx/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()


def main():
    print(get_value('X'))

if __name__ == '__main__':
    main()
