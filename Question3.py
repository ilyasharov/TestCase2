def quicksort(array):
    if len(array) <= 1:
        return array

    pivot = array[-1]  # Выбор опорного элемента
    smaller = [x for x in array if x <= pivot]
    larger = [x for x in array if x > pivot]

    return quicksort(smaller) + [pivot] + quicksort(larger)