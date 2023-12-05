def second_largest(arr):
    sorted_arr = sorted(arr, reverse=True)
    return sorted_arr[1] if len(sorted_arr) > 1 else None

numbers = [10,8,88,99,7,78]
result = second_largest(numbers)
if result:
    print("the second largest:",result)
else:
    print("no second largest")