'''
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''
def pattern1():
    for i in range(1,int(input("1 Enter Range: "))+1):
        for j in range(i):
            print(i,end=" ")
        print("")
#pattern1()
'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
'''
def pattern2():
    for i in range(1,int(input("2 Enter Range: "))+1):
        for j in range(i):
            print(j,end=" ")
        print('')
#pattern2()
'''
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5
'''
def pattern3():
    n = int(input("3 Enter Range: "))
    for i in range(1, n + 1):
        for j in reversed((range((n+1)-i))):
            print(i,end=" ")
        print("")
#pattern3()
'''
5 5 5 5 5 
5 5 5 5 
5 5 5 
5 5 
5
'''
def pattern4():
    n = int(input("4 Enter Range: "))
    for i in range(1, n + 1):
        for j in reversed((range((n+1)-i))):
            print(n,end=" ")
        print("")
#pattern4()
'''
5 5 5 5 5
5       5
5       5
5       5
5 5 5 5 5
Only for single digit numbers.
'''
def pattern5():
    n=int(input("5 Enter range: "))
    for i in range(n):
        for j in range(n):
            if i==0 or i==n-1:
                print(n,end=" ")
            else:
                if j==0 or j==n-1:
                    print(n,end=" ")
                else:
                    print(" ",end=" ")
        print("")
#pattern5()
'''
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1
'''
def pattern6():
    n=int(input("6 Enter Range: "))
    for i in range(1,n+1):
        for j in reversed(range((n-i)+1)):
            print((n+1-i),end=" ")
        print("")
#pattern6()
'''
1 
1 2 
1 2 4 
1 2 4 8 
1 
2 1 
4 2 1 
8 4 2 1  
'''
def pattern7():
    n=int(input("7 Enter range: "))
    for i in range(1,n+1):
        k=1
        for j in range(1,i):
            print(k,end=" ")
            k=k*2
        print("")
    rows = n
    for i in range(1, rows):
        for j in range(-1 + i, -1, -1):
            print(2 ** j, end=' ')
        print("")
#pattern7()
'''
1 
1 2 
1 2 4 
1 2 4 8 
1 2 4 8 16 
1 2 4 8 
1 2 4 
1 2 
1 
'''
def pattern8():
    n=int(input("8 Enter Range: "))
    for i in range(n+1):
        for j in range(i):
            print(2**j,end=" ")
        print("")
    for i in range(1,n):
        for j in range(n-i):
            print(2**j,end=" ")
        print("")
#pattern8()
'''
* 
** 
*** 
**** 
***** 
**** 
*** 
** 
* 
'''
def pattern9():
    n=int(input("9 Enter Range:" ))
    for i in range(1,n+1):
        print("*"*i,end=" ")
        print("")
    for i in range(n-1,0,-1):
        print("*"*i,end=" ")
        print("")
#pattern9()