pick = 6

left = 1
right = 10

while left <= right:
    mid = (left + right) // 2

    if mid == pick:
        print(mid)
        break
    elif mid < pick:
        left = mid + 1
    else:
        right = mid - 1
