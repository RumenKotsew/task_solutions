def magic_square(square):
    amount = sum(square[0])
    for row in square:
        current_amount = sum(row)
        if current_amount != amount:
            return False

    for col_index in range(len(square)):
        current_amount = walk_col(col_index, square)
        if current_amount != amount:
            return False

    current_amount = walk_diag_right_down(square)
    if current_amount != amount:
        return False

    current_amount = walk_diag_left_down(square)
    if current_amount != amount:
        return False

    return True


def walk_col(col_index, square):
    return sum([square[row][col_index] for row in range(len(square))])


def walk_diag_right_down(square):
    return sum(square[index][index] for index in range(len(square)))


def walk_diag_left_down(square):
    return sum([square[len(square) - 1 - index][index] for index in range(len(square))[::-1]])


good_example = [
    [23, 28, 21],
    [22, 24, 26],
    [27, 20, 25]
]

bad_example = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(magic_square(good_example))
print(magic_square(bad_example))
