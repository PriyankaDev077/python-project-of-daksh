#input the number of rows
N = int(input("enter the number of rows:"))
#input the numbers of column
M = int(input("enter the number of column:"))
for i in range(1,N,2): #iterate for loop
    print((i *".|.").center(M,"-")) #display output
print("WELCOME".center(M, "-"))
for i in range(N-2, -1, -2):
    print((i *".|.").center(M, "-"))
