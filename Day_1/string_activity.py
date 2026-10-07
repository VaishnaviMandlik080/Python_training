# Q1. Extract "code" from the given string
S = "Sample python code"
print(S[-4:])

# Q2. Given a string S = "x:y:z"
S = "x:y:z"

# (i) Display the last 2 characters
print(S[-2:])

# (ii) Display the total string length
print(len(S))

# Q3. Remove newline, tab and colon characters
S1 = "root:x:bin:bash\n"
S2 = "root:x:bin:bash\t"
S3 = "root:"

print(S1.replace("\n", "").replace(":", ""))
print(S2.replace("\t", "").replace(":", ""))
print(S3.replace(":", ""))