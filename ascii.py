n = int(input("enter the number : "))
str_=""
for i in range(n):
    x = int(input(f"enter {i+1} character:"))
    str_+=(chr(x))
print(str_)