def minion_game(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    string = string.upper()
    stuart = []
    stuart_string = ''
    for i in range(len(string)):
        if string[i] not in vowels:
            for j in string[i:]:
                stuart_string += j
                stuart.append(stuart_string)

        stuart_string = ''
    # print(stuart)
    stuart_score = len(stuart)
    kevin = []
    kevin_string = ''
    for i in range(len(string)):
        if string[i] in vowels:
            for j in string[i:]:
                kevin_string += j
                kevin.append(kevin_string)
        kevin_string = ''

    kevin_score = len(kevin)

    if kevin_score > stuart_score:
        print('Kevin {}'.format(kevin_score))
    elif kevin_score == stuart_score:
        print('Draw')
    else:
        print('Stuart {}'.format(stuart_score))


if __name__ == '__main__':
    s = input()
    minion_game(s)
