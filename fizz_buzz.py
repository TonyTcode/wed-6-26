number = int(input("Enter Number "))

if number % 3 == 0:
  print("Fizz")

if number % 5 == 0:
  print("Buzz")

if number % 3 == 0 and number % 5 == 0:
  print("Fizz Buzz")
  