import sys

def mergeSort(oldList):
    if len(oldList) > 1:
        middle_point = len(oldList)//2

        # Split the lists
        left = oldList[:middle_point]
        right = oldList[middle_point:]

        # Recursively sort the arrays!
        mergeSort(left)
        mergeSort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                oldList[k] = left[i]
                i+=1
            else:
                oldList[k] = right[j]
                j+=1
            k+=1

        # Check if there are any elements left
        while i < len(left):
            oldList[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            oldList[k] = right[j]
            j+=1
            k+=1
