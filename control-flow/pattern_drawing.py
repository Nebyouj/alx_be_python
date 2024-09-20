size_of_the_pattern = int(input("Enter the size of the pattern: "))

i = 0
while i < size_of_the_pattern:
    for j in range(size_of_the_pattern):
        print("*", end = "")
    print()
    i += 1