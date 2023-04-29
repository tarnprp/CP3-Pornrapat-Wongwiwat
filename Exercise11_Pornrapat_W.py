number = int(input())
for x in range(number):
    x = x+1
    print(" "*(number-x), "*"*((2*x)-1))