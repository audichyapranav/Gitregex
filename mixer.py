def input_String(username , password):
 username = "Pranav"
 password = "12345"
 count = 0

for i in input_String:
	count = count + 1
newString = input_String[ 0:2 ] + input_String [count - 2: count ]

print("Input string = " + input_String)
print("New String = "+ newString)
