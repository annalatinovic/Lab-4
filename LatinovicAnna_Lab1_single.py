def C():
    n = int(input("Please enter an integer value for n:"))
    count = 0

    while n >= 1:
        if(n%2 == 0):
            n = n/2
            print(int(n), end = " ")
            count = count + 1
            if n == 1:
                break
        else: 
            n = (3*n) + 1
            print(int(n), end = " ")
            count = count + 1
            if n == 1:
                break
    print("\nThe number of iterations needed to reach one is: " + str(count))

C()