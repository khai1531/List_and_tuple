def find_two_largest(numbers):

  if len(numbers) < 2:
    raise ValueError("Danh sách phải có ít nhất 2 phần tử.")

  sorted_list = sorted(numbers)
  return sorted_list[-2:]
  max1 = None
  max2 = None
  for num in numbers:
    if max1 is None or num > max1:
      max1 = num
    elif max2 is None or num > max2:
      max2 = num
  return max1, max2

numbers = [5, 2, 4, 1, 3]
largest_two = find_two_largest(numbers)
print(f"Hai số lớn nhất trong danh sách {numbers} là: {largest_two}")
