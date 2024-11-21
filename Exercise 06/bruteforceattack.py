#Give the expected password for verification
expected_password = "12345"

#GIVE the maximum number of attempts
maximum_limit = 5
limit = 0

#again again ask for password until it reaches maximum number of attempts
while limit < maximum_limit:

    #aquire the password from the user 
    password_attempt = input("Type your password:")

    #Verifying the entered password matches
    if password_attempt == expected_password:
     print("Password Correct. have  your access!")
     break
    else:
        #making the number of attempts more
         limit += 1
         attempts_left = maximum_limit - limit
         if attempts_left > 0:
            print("Incorrect password. You have " + str(attempts_left) + " remaining tries.")
         else:
            print("Incorrect password. You've reached the attempt limit. The authorities have been notified.")