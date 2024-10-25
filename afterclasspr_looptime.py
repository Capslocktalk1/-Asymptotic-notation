def Complexity(n):

    for i in range(0, n+1):  # O(n)
        print("First Loop")

    j = 1
    while j <= n+1:  # O(log n)
        print("Second Loop ", j)
        j = j * 2

    for i in range(0, 100):  # O(1)
        print("Third Loop")

    print("\nTime Complexity of First Loop: O(n)")
    print("Time Complexity of Second Loop: O(log n)")
    print("Time Complexity of Third Loop: O(1)")

Complexity(10)
