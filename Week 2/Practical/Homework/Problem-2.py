#Problem 2
text = input()
mid = int((len(text)-1)/2)
print("The old string:" ,text)
print("Middle 3 characters:" ,text[mid-1:mid+2])
print("The new string:" ,text[:mid-1] + text[mid-1:mid+2].upper() + text[mid+2:])