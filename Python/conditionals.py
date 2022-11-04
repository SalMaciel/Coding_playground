x = 2
y = 5

# Conditionals
if x == 2:
    print("x is equal to 2")
if y != 2:
    print("y is not iqual to 5")
if x < y:
    print("x is less than y")
if y > x:
    print("y is greater than x")
if x >= 2:
    print("x is greaer or equal to 2")

# I can have more than one condition
if x == 2 and y == 5:
    print("x value and y value are true")
if x < 20 or y < 8:
    print("at least x or y is true")

# Nested if statements
if x < 8:
    if y < 6:
        print("x is less than 8 and y is less than 6")
    elif y == 5:
        print("x is less than 8 and y is equal to 5")
    else:
        print("x is less than 8 and y greater or equal to 5")
else:
    print("x is greater or equal to 8")