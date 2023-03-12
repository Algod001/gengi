def binary_search(list, first, last, match):
    if first > last:
        return "not found"
    
    mid = (first + last) // 2
    if list[mid] == match:
        return mid + 1
    elif list[mid] > match:
        return binary_search(list, first, mid - 1, match)
    else:
        return binary_search(list, mid + 1, last, match)


def main():
    lst = [1, 2, 4, 6, 8, 10]
    search = 2
    print(binary_search(lst, 0, len(lst) - 1, search))


main()
