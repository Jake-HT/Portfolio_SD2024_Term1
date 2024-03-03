class SortFunctions:

    def __init__(self) -> None:
        pass

    def bubble_sort(self,arr):
        n = len(arr) # declares the length of the array as 'n'

        for i in range(n): # for index in length of array

            for j in range(0, n-i-1): # for jindex in (starts at index 0, n is the total number of elements in the array, i is the current number of iterated and therefor sorted elements, and -1 is there to ensure the loop stays within bounds)

                if arr[j] > arr[j+1]: # if current indexed item in array is greater than next indexed item in array,
                    arr[j], arr[j+1] = arr[j+1], arr[j] # swaps items
        return arr #when all is said and done, return sorted array

    def insertion_sort(self,arr):
        for i in range(1, len(arr)): # for index in 
            key = arr[i]

            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]  
                j -= 1

            arr[j + 1] = key
        return arr

    def selection_sort(self,arr):
        for i in range(len(arr)):
            
            min_index = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j

            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr

    def merge_sort(self,arr):
        if len(arr) > 1:
            mid = len(arr) // 2 
            left_half = arr[:mid]
            right_half = arr[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1
        return arr

    def quick_sort(self,arr):
        if len(arr) <= 1:
            return arr 

        pivot = arr[len(arr) // 2]  
        left = [x for x in arr if x < pivot] 
        middle = [x for x in arr if x == pivot] 
        right = [x for x in arr if x > pivot] 

        return self.quick_sort(left) + middle + self.quick_sort(right)  