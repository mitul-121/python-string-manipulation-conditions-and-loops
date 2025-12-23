numbers= list(map(int,input("Enter random numbers: ").split()))
print(numbers)

largest=numbers[0]
smallest=numbers[0]

for number in numbers:
    if number > largest:
        largest=number
    if number < smallest:
        smallest=number

print(largest, smallest)

