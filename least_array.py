numbers = [7, 9, 6 ,3, 72, 1003, 67,]
n = len(numbers)

def least_array(numbers,n):

  min_number = numbers[0]
  
  for index in range(1,n):
    if index < min_number:
      min_number = numbers[index]
  return min_number

min_array = least_array(numbers,n)

print(min_array)