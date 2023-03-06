def head(l):
    return l[0]


print(head([1, 2, 3, 4]))


def last(l):
    return l[-1]


print(last([1, 2, 3, 4]))


def tail(l):
    return l[1:]


print(tail([1, 2, 3, 4]))


def equal_list(left, right):
    if type(left) != list or type(right) != list:
        raise Exception("We need two lists!")
    return left == right


print(equal_list([1, 2, 3, 4], [1, 2, 3, 4]))


def count_item(digit, l):
    counter = 0
    for item in l:
        if item == digit:
            counter += 1
    return counter
# return l.count(digit)


print(count_item(5, [1, 2, 3, 4, 5]))


def take(digit, l):
    return l[:digit]


print(take(2, [1, 2, 3, 4, 5]))


def drop(digit, l):
    return l[digit:]


print(drop(1, [3, 2, 3]))


def reversed_list(l):
    return l[::-1]


print(reversed_list([1, 2, 3, 4]))
