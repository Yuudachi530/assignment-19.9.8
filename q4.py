UserList = []
PasswordList = []
MaxIndex = 20
MyUserID = str(input("enter an UserID: "))
MyPassword = str(input("enter the Password: "))
UserIdFound = False
LoginOK = False
Index = 0
while Index != 20 or UserIdFound != True:
    Index = Index + 1
    if UserList[Index] == MyUserID:
        UserIdFound = True
        
if UserIdFound == True:
    if PasswordList[Index] == MyPassword:
        LoginOK = True

if LoginOK == True:
    print("Login Successful")
else:
    print("User ID and/or password incorrect")