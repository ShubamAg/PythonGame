'''def merge_sort(arr, merge):
    if len(arr)<=1:
        return arr
    mid = len(arr//2)
    left_half= merge_sort(arr[:mid])
    right_half= merge_sort(arr[mid:])
    return merge(left_half,right_half)
def merge (left,right):
    sorted_arr=[]
    i=j=0
    
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i+=1
        else:
            sorted_arr.append(right[j])
            j+=1
            
            sorted_arr.extend(left[i:])
            sorted_arr.extend(right[j:])
            return sorted_arr
        arr= [9,6,4,8,3,1,2,7]
        sorted_arr= merge_sort(arr)
        print("Sorted Array :" ,sorted_arr)'''
        
def merge_sort(arr):
    if len(arr) <= 1:
        return arr 
    # Base case: A list with 0 or 1 element is already sorted
    
    # Step 1: Split the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])   
    # Recursively sort the left half
    
    right_half = merge_sort(arr[mid:])  
    # Recursively sort the right half
    
    # Step 2: Merge the two sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    sorted_arr = [] 
    # This will store the merged sorted elements
    
    i = j = 0  
    # Pointers for left and right halves
    
    # Compare elements from both halves and add the smallest one to sorted_arr
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # If there are any remaining elements in the left or right half, add them
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    
    return sorted_arr

# Example usage
arr = [6, 3, 8, 5, 2, 7, 4, 1]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
