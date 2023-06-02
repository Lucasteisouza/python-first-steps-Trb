def is_anagram(first_string, second_string):
    if type(first_string) != str or type(second_string) != str:
        return (first_string, second_string, False)
    if first_string == '' and second_string == '':
        return (first_string, second_string, False)
    first_list = list(first_string.lower())
    second_list = list(second_string.lower())
    quicksort(first_list)
    quicksort(second_list)
    if len(first_list) != len(second_list):
        return (''.join(first_list), ''.join(second_list), False)
    if first_list == second_list:
        return (''.join(first_list), ''.join(second_list), True)
    else:
        return (''.join(first_list), ''.join(second_list), False)


def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if len(array) == 1:
        return array

    if low < high:
        partition_index = partition(array, low, high)
        quicksort(array, low, partition_index - 1)
        quicksort(array, partition_index + 1, high)


def partition(array, low, high):
    i = low - 1
    pivot = array[high]

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1
