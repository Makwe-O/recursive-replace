main_string = input("Please enter a string: ")
sub_string = input("Please enter the sub string you wish to find: ")
replace_string = input("Please enter a strig to replace the given substring:")


def rec_replace(string, a, b):
    # if the string is empty
    if not string:
        return ""
    elif string[:len(b)] == b:
        return a + rec_replace(string[len(b):], a, b)
    else:
        return string[0] + rec_replace(string[1:], a, b)


print(rec_replace(main_string, replace_string, sub_string))
