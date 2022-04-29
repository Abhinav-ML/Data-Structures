# Approach 1 : By using slicing
str1 = input("Enter the string")
print(str1[::-1])
print() #for creating new line

# Approach 2 : By traversing the whole string and store its element into new variable

s = input("Enter the string :\n")
rev = ""
for element in s:
    rev = element + rev
print(rev)
