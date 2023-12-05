def second_smallest(numbers):
    sorted_numbers = sorted(set(numbers))
    return sorted_numbers[1] if len(sorted_numbers) > 1 else None

my_list = [10, 5, 8, 20, 15]
result = second_smallest(my_list)

if result is not None:
    print("second smallest number:",result)
else:
    print("no second smallest number")


