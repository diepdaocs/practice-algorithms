# Write a quick sort function that sort a list of numbers
def quick_sort(nums):
    if len(nums) <= 1: return nums # base case, no need to sort anything
    
    pivot = nums[0] # choose the first element as the pivot
    left = [x for x in nums[1:] if x < pivot] # all elements less than the pivot go to the left
    right = [x for x in nums[1:] if x >= pivot] # all elements greater than or equal to the pivot go to the right
    
    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort([3, 2, 1, 4, 5])) # should print [1, 2, 3, 4, 5]
print(quick_sort(['b', 'c', 'a'])) # Should print ['a', 'b', 'c']
print(quick_sort([2, 3, 5, 7, 13, 11])) # should print [2, 3, 5, 7, 11, 13]
