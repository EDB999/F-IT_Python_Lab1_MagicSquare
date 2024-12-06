flag = False


def createSquare():
    n = int(input())

    square = []

    for i in range(n):
        row = []
        for j in range(n):
            number = int(input(f"Write the element of the Magic Square by index - {i}, {j}: "))
            row.append(number)
        square.append(row)
        print("\n")

    for row in square:
        print(" ".join(map(str, row)), end="\n")
    print()

    return square


def checkMagicSquare(square):
    n = len(square)

    row_sums = [sum(row) for row in square]

    column_sums = [sum(square[i][j] for i in range(n)) for j in range(n)]

    diagonal_sums = [sum(square[i][i] for i in range(n))]

    side_diagonal_sums = [sum(square[i][n - i - 1] for i in range(n))]

    if all(x == row_sums[0] for x in row_sums + column_sums + diagonal_sums + side_diagonal_sums):
        print(f"Yes, it's the Magic Square\n", end="\n")
        return True
    else:
        print(f"No, isn't the Magic Square\n", end="\n")
        return False


def checkMaxElement(square):
    n = len(square)

    saddle_points = []

    max_element_row = [max(row) for row in square]
    min_element_column = [min(square[i][j] for i in range(n)) for j in range(n)]

    saddle_points.append(max_element_row)
    saddle_points.append(min_element_column)

    if saddle_points:
        print(f"Yes, Magic Square has saddle points max in rows, min in columns: {saddle_points}\n")
    else:
        print(f"No, Magic Square hasn't saddle points max in rows, min in columns\n")


def checkMinElement(square):
    n = len(square)

    saddle_points = []

    min_element_row = [min(row) for row in square]

    max_element_column = [max(square[i][j] for i in range(n)) for j in range(n)]

    saddle_points.append(min_element_row)
    saddle_points.append(max_element_column)

    if saddle_points:
        print(f"Yes, Magic Square has saddle points max in columns, min in rows: {saddle_points}\n", end="\n")
    else:
        print("No, Magic Square hasn't saddle points max in columns, min in rows\n", end="\n")


if __name__ == '__main__':
    magic_square = createSquare()

    flag = checkMagicSquare(magic_square)

    if flag:
        checkMaxElement(magic_square)

        checkMinElement(magic_square)
