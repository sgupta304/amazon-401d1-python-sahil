def reverse_list(input_list):
    new_list = []
    for current_value in input_list[::-1]:
        new_list.append(current_value)
    return new_list


if __name__ == '__main__':
    a = [1, 3, 4, 5, 6, 8]
    b = [89, 2354, 3546, 23, 10, -923, 823, -12]
    c = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
         37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
         79, 83, 89, 97, 101, 103, 107, 109, 113,
         127, 131, 137, 139, 149, 151, 157, 163,
         167, 173, 179, 181, 191, 193, 197, 199,
         200, 201, 202, 203, 204, 205, 206, 207]
    d = []
    e = [1]
    f = ["One", "Two", "Three", "Four", "Five"]
    print(reverse_list(a))
    print(reverse_list(b))
    print(reverse_list(c))
    print(reverse_list(d))
    print(reverse_list(e))
    print(reverse_list(f))
