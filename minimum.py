def minimum(array):
    num_of_rows = len(array)
    num_of_cols = len(array[0])
    result = []

    #минимальная сумма в строках
    row = {i : sum(array[i]) for i in range(num_of_rows)}
    result.append(min(row, key=row.get))

    #минимальная сумма в колонках
    columns = {}
    for i in range(num_of_cols):
        sumC = 0
        for j in range(num_of_rows):
            sumC += array[j][i]
            columns.update({i : sumC})
    
    minCol = min(columns, key=columns.get)
    result.append(minCol)

    return result

print(minimum([[7, 2, 7, 2, 8],
               [2, 9, 4, 1, 7],
               [3, 8, 6, 2, 4],
               [2, 5, 2, 9, 1],
               [6, 6, 5, 4, 5]]))

print(minimum([[-7, -2, -7, -2, -8],
               [-2, -9, -4, -1, -7],
               [-3, -8, -6, -2, -4],
               [-2, -5, -2, -9, -1],
               [-6, -6, -5, -4, -5]]))
