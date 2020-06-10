# puts the number's digits in ascending...
def asc(n):
    return int(''.join(sorted(str(n))))

# ...and descending order
def desc(n):
    return int(''.join(sorted(str(n))[::-1]))

# asks for the number
n = input("Specify a number: ")
print ("\nTransforming", n)

# iterates, assigns the new diff
while n != desc(n) - asc(n):
    print (desc(n), "-", asc(n), "=", desc(n)-asc(n))
    n = desc(n) - asc(n)

# prints the ultimate number, if it can
print ("Kaprekar reached:", n)
