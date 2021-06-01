def bracket_validation(data):
    open_brackets = ['{', '(', '[']
    close_brackets = ['}', ')', ']']
    list = []

    for i in data:
        if i in open_brackets:
            list.append(i)

        elif i in close_brackets:

            indexes = close_brackets.index(i)

            if len(list) > 0 and open_brackets[indexes] == list[len(list)-1]:
                list.pop()
            else:
                return False

    if len(list) == 0:
        return True
    else:
        return False


print(bracket_validation('{}'))
print(bracket_validation('{}(){}'))
print(bracket_validation('()[[Extra Characters]]'))
print(bracket_validation('(){}[[]]'))
print(bracket_validation('{}{Code}[Fellows](())'))
print(bracket_validation('[({}]'))
