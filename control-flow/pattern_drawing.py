

size_of_pattern = int(input("Enter the size of the pattern: "))
size_of_pattern_new = size_of_pattern + 1
x=1
while x < size_of_pattern_new :
    for i in range(size_of_pattern):
        print("*", end="")
    print()
    x+=1


