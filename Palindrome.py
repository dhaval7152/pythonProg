# number=int(input("Enter the No:"))
# number=121
# temp=number
# reverse=0

# while(number>0):
#     dig=number%10
#     reverse=reverse*10+dig
#     number=number//10
# if(temp==reverse):
#     print("It a palindrome number")
# else:
#     print("Not a palindrome number")

# For String
# def isPalindrome(s):
#     return s == s[::-1]

# s=input("Enter String: ")
# ans=isPalindrome(s)
# if ans:
#     print("yes it is")
# else:
#     print("it's not")



# Python program to check
# if a string is palindrome
# or not
 
x = "malayalam"
w = ""
for i in x:
    w = i + w
if (x == w):
    print("Yes")
else:
    print("No")