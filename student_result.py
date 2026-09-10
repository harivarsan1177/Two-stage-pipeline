mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))

total = mark1 + mark2 + mark3
average = total / 3

print("Total =", total)
print("Average =", average)

if mark1 >= 40 and mark2 >= 40 and mark3 >= 40:
    print("Result = PASS")
else:
    print("Result = FAIL")