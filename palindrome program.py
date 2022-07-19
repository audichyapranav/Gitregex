
val = input("enter number")
if (int(val) == int(val[-1::-1])):
    print("the number is palindrome")
else:
        print("number is not a palindrome")