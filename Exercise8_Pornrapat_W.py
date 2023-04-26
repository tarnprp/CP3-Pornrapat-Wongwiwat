print("Hello. Please login to use the system")
username = input("Username = ")
password = input("Password = ")
if username == "admin" and password == "1234" :
    print("Login Successfully!")
    print("Welcome!")
    print("What would you like to buy?")
    print("1. Banana (7 THB each)")
    print("2. Apple (10 THB each)")
    print("3. Kiwi (16 THB each)")
    select = int(input("Number "))
    if select == 1:
        print("How many?")
        banana = int(input())
        print(7 * banana,"THB.")
    if select == 2:
        print("How many?")
        apple = int(input())
        print(10 * apple, "THB.")
    if select == 3:
        print("How many?")
        kiwi = int(input())
        print(16 * kiwi, "THB.")
    print("Thank you for buying.")
else :
    print("Error, please try again.")