#Problem 4
text = input()
x = text.count("USA")
y = text.count("usa")
z = text[:11] + text[11:14].lower() + text[14:]
print("The given string:" ,text)
print("The USA/usa count is:" ,x + y)
print("The new string:" ,z.replace("usa","Armenia"))