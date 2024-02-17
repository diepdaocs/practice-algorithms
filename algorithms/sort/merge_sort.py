# Implement the merge source function
def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case
    
    mid = int(len(arr) / 2) # Divide the array into two halves
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    
    i, j = 0, 0
    result = []
    
    while i < len(left) and j < len(right): # Merge the sorted halves
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result += left[i:] + right[j:]  # Append remaining elements
    return result

# Test the function with a sample input
arr = [6, 5, 4, 3, 2, 1]
print(merge_sort(arr))

# Output: [1, 2, 3, 4, 5, 6]