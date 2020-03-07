def BinarySearch(array, searchElement):
    start=0
    end= len(array)-1
    while(start <= end):
        mid = (start + end) // 2
        if array[mid] == searchElement:
            return searchElement
        elif array[mid] < searchElement:
            start = mid+1
        else:
            end = mid-1 
    return -1   