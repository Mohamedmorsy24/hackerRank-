if __name__ == '__main__':
    N = int(input())
    main_list = []
    for i in range(N):
        lst = input().split(' ')
        if lst[0] == 'insert':
            main_list.insert(int(lst[1]), int(lst[2])) ##
        elif lst[0] == 'print':
            print(main_list)
        elif lst[0] == 'remove':
            main_list.remove(int(lst[1]))           ##
        elif lst[0] == 'append':
            main_list.append(int(lst[1]))           ##
        elif lst[0] == 'sort':
            main_list.sort()
        elif lst[0] == 'pop':
            main_list.pop()
        elif lst[0] == 'reverse':
            main_list.reverse()


