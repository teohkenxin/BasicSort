def selection_sort(array):
    for border in range(0, len(array)):
        min = border
        for pointer in range(border+1, len(array)):
            if array[pointer] < array[min]:
                min = pointer
        array[min],array[border] = array[border],array[min]
    return array


def bubble_sort(array):
    for i in range(0, len(array)): 
        for number in range (0, len(array)-i-1): 
            if array[number] > array[number+1]:
                array[number+1], array[number] = array[number], array[number+1] 
    return array

def insertion_sort(array):
    for border in range(1, len(array)): #start from index 1 until the end.
        last_index = border-1 #the index of the first number in front of the border
        newMember = array[border] #the first number behind the border
        while last_index >= 0 and array[last_index] > newMember: #while last_index is not lower than 0 and array[last_index] is bigger than the newMember 
            array[last_index+1] = array[last_index] #push array[last_index] to array[last_index + 1]
            last_index -= 1 #minus tail_index, repeat until it becomes lower than 0 (which breaks the loop)
        array[last_index+1] = newMember
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