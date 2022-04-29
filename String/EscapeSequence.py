# we can print single quote inside double quote and vice-versa
sentence = "This is Abhinav's phone"
print(sentence)
sentence1 = 'This is Abhinav"s phone'
print(sentence1)

# we can use escape character i,e. \ (backward slash)
sentence2 = 'This is Abhinav\'s phone'
print(sentence2)

sentence3 = 'This is \ Abhinav\\n\'s phone'
print(sentence3   )


###########    RAW String   ##########

# We can create a raw string in python by either using a small r or a capital R before the string literal.

s1 = "c:\project\name.py"
s2 = r"c:\project\name.py"
print(s1)
print(s2)
