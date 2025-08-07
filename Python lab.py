def validemail(y):
    if "@" and "." in y:
        for i in range(len(y)):
            if "@" == y[i]:
                g=i
                continue
            if "." == y[i]:
                k=i
                continue

        if k > g+1 and g > 0 and k+1 < len(y):
            return True
        else:
            return False
    else:
        return print("Not valid2")
    


for i in range(5):
    y = input("Enter you mail adress:")
    if validemail(y) == True:
        print("welcome")
        break
    else:
        print("Try again")
        
else:
    raise TypeError("You are blocked")
    