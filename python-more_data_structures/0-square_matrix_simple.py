#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [0] * len(matrix)
    new_list = [0] * len(matrix[0])
    for i in range(len(matrix)):
        for b in range(len(matrix[i])):
            new_list[b] = (matrix[i][b]) ** 2
        new_matrix[i] = new_list[0: len(new_list)]
    return(new_matrix)
