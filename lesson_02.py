password = "q1w2e3r4"
x = 3
while x > 0:
    P = input("Enter password:")
    x -= 1  # х = x-1
    if P == password:
        print("Access granted")
        break
    if x == 0:
        print("You have no attempts left")
    else:
        print("Access denied, attempts left:", x)
