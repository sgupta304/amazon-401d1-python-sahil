def insert_shift_array(arr, val):
    """
    Inserts value into give array at mid point
    :param arr: Any sequence that can be converted to a list
    :param val: Value to insert
    :return: New list with value inserted into middle
    """
    lst = list(arr)
    mid = (len(lst) + 1) // 2
    return lst[:mid] + [val] + lst[mid:]
