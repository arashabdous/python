def _sum_of_a_2d_list_sample_(sample_2d_list):
    total_SUM = 0
    number_of_rows = len(sample_2d_list)
    number_of_columns = len(sample_2d_list[0])
    rows = 0
    c = 1
    while rows < number_of_rows:
        columns = 0
        while columns < number_of_columns:
            total_SUM = total_SUM + sample_2d_list[rows][columns]
            columns = columns + 1
            c = c + 1
            rows = rows + 1
    return c


x = input("input 2D list: ")
# print(_sum_of_a_2d_list_sample_(x))
print(_sum_of_a_2d_list_sample_(x))
