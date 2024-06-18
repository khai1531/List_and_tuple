def find_two_largest(numbers):
  """
  Tìm hai số lớn nhất trong danh sách.

  Args:
    numbers: Danh sách các số.

  Returns:
    Tuple chứa hai số lớn nhất (số lớn nhất trước, số lớn thứ hai sau).
  """
  if len(numbers) < 2:
    raise ValueError("Danh sách phải có ít nhất 2 phần tử.")

  # Cách 1: Sử dụng phương pháp sắp xếp
  sorted_list = sorted(numbers)
  return sorted_list[-2:]

  # Cách 2: Sử dụng hai biến để so sánh
  max1 = None
  max2 = None
  for num in numbers:
    if max1 is None or num > max1:
      max1 = num
    elif max2 is None or num > max2:
      max2 = num
  return max1, max2

# Ví dụ sử dụng
numbers = [5, 2, 4, 1, 3]
largest_two = find_two_largest(numbers)
print(f"Hai số lớn nhất trong danh sách {numbers} là: {largest_two}")
