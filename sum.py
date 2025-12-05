no_of_inputs = int(input("Enter the no of numbers: "))
count = 0
even_numbers = 0
odd_numbers = 0

while count < no_of_inputs:
    numbers = int(input("Enter a number: "))
    count += 1

    if(numbers % 2 == 0):
        even_numbers += numbers
    else:
        odd_numbers += numbers
print("Sum of even numbers is ", even_numbers, "and sum of odd numbers is ", odd_numbers)

