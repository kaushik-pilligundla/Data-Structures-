# Finding the floor of a number with binary search

arr = [2, 3, 4, 9, 14, 16, 18]
s = 0
e = len(arr) - 1
target = 15

while s < e:
    mid = (s+e) // 2
    if arr[mid] == target:
        print(arr[mid])
        break
    elif arr[mid] < target:
        s = mid + 1
    else:
        e = mid - 1

else:
    print(e)  # printing the end as we're looking for greatest number smaller than the target if target is not found
