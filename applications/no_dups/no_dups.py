def no_dups(s):
    # Your code here
    s = s.split()

    new_dict = {}

    for i in s:
        if i not in new_dict:
            new_dict[i] = 0

    new_string = ""

    dict_items = new_dict.items()

    for item in dict_items:
        new_string += f"{item[0]} "

    return new_string.strip()


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
