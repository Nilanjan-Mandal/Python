N = int(input("Please enter the range: "))
i = 0
for i in range(i, N+1):
    if(i % 2 == 0):
        print(i)
        i = i + 1


M = int(input("Please enter the range for odd numbers: "))
j = 0
for j in range(j, M+1):
    if(j % 2 != 0):
        print(j)
        j = j + 1
