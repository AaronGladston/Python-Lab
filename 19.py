str1=list(input("Enter the first string:\n"))
str2=list(input("Enter the second string:\n"))
temp=str1[1]
str1[1]=str2[1]
str2[1]=temp
print("The concatenated string is:\n",''.join(str1)+''.join(str2))
