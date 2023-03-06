def sublist_greasy(list1, list2):
    return str(list1)[2:-2] in str(list2)[2:-2]


def sublist(list1, list2):
    if not list1:
        return True
    for main_index in range(len(list2)):
        if list2[main_index] == list1[0]:
            if do_the_check(list1, list2, main_index + 1, 1):
                return True
    return False


def do_the_check(list1, list2, main_index, inner_index):
    while main_index < len(list2):
        if inner_index >= len(list1):
            return True
        if list1[inner_index] != list2[main_index]:
            return False
        main_index += 1
        inner_index += 1
    return True


print(sublist(["Python"], ["Python", "Django"]))
print(sublist([1, 2, 3], [0, 0, 1, 2, 3, 5, 6]))
print(sublist([], [1, 0, 1, 2, 2]))
