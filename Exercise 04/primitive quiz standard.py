"""In this exercise, you’ll create a simple program that asks the user a question,
evaluates their answer, and provides feedback.
Steps:
1. Write a program that asks the user “What is the capital of France?” and
waits for their response.
2. If the user’s answer is correct (i.e., “Paris”), the program should print a
message saying the answer is correct.
3. If the answer is incorrect, the program should print a message saying the
answer is wrong."""

#Step 1
#Writing a program that asking the user "What is the capital of France?" and waiting for their response
Question = input("What is the capital of France?")

#Step 2
#Printing a message saying the answer is correct if the user's answer is correct
if Question == "paris":
    print("The answer is correct")

#Step 3
#Printing a message saying the answer is incorrect if the user's answer is incorrect
else:
    print("The answer is incorrect")
