#Problem 2
text = input()
text1 = text[3:6]
text2 = text[0:3] + text[3:6].upper() + text[6:]
print("The old string:" ,text)
print("Middle 3 characters:" ,text1)
print("The new string:" ,text2)