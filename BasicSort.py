def selection_sort(array):
    for border in range(0, len(array)):
        min = border
        for pointer in range(border+1, len(array)):
            if array[pointer] < array[min]:
                min = pointer
        array[min],array[border] = array[border],array[min]
    return array


def bubble_sort(array):
    for first_number in range(0, len(array)):
        for second_number in range (first_number+1, len(array)):
            if array[second_number] < array[first_number]:
                array[second_number], array[first_number] = array[first_number], array[second_number]
    return array

def insertion_sort(array):
    for border in range(1, len(array)):
        last_value = border-1
        newMember = array[border]
        while last_value >= 0 and array[last_value] > newMember:
            array[last_value+1] = array[last_value]
            last_value -= 1
        array[last_value+1] = newMember
    return array

unordered = [64, 25, 12, 22, 11]

ordered = selection_sort(unordered.copy())
print("[selection sort result]")
print (ordered,"\n")

ordered = bubble_sort(unordered.copy())
print("[bubble sort result]")
print (ordered,"\n")

ordered = insertion_sort(unordered.copy())
print("[insertion sort result]")
print (ordered)