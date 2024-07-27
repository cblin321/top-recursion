import math
def mergesort(unsorted):
    if not unsorted or len(unsorted) == 1:
        return unsorted
    
    left = mergesort(unsorted[:math.floor(len(unsorted) / 2)])
    right = mergesort(unsorted[math.floor(len(unsorted) / 2):])
    return merge(left, right)

def merge(left, right):
    left_pointer = 0
    right_pointer = 0
    merged = []
    
    while left_pointer < len(left) and right_pointer < len(right):
        to_add = min(left[left_pointer], right[right_pointer])
        if to_add == left[left_pointer]:
            left_pointer += 1
        else:
            right_pointer += 1    
        merged.append(to_add)
        
    merged += left[left_pointer:]
    merged += right[right_pointer:]
    
    return merged


print(mergesort([3, 2, 1, 13, 8, 5, 0, 1]))
print(mergesort([105, 79, 100, 110]))
