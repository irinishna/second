password = "q1w2e3r4"
while x <= 3 :
    P = input("Enter password:")
    x += 1
    if P == password :
        print("Access granted")
        break
    else :
        print("Access denied, attempts left:", )