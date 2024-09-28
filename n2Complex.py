def printNumber(n):
    itr = 0
    print("The number user enbtered: ", n)
    for i in range(0,n):
        for j in range(0,n):
            print("*", end="")
            itr+=1
        print("")
    print("The iteration done by this code: ", itr)
    
printNumber(5)