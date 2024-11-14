#A list containing 10 questions asking for the capitals of 10 European countries.
Countries_with_capitals = [
    "What is  capital of France?", 
    "What is  capital of United Kingdom?", 
    "What is  capital of germany?",
    "What is  capital of spain?",
    "What is  capital of austria?", 
    "What is  capital of Italy?",
    "What is  capital of netherlands?", 
    "What is  capital of Greece?",
    "What is  capital of sweden?", 
    "What is  capital of Belgium?"
]

#answers of the above 10 questions
right_answers = [
  "paris",
  "london",
  "Berlin",
  "madrid",
  "vienna",
  "rome",
  "amsterdam",
  "athens",
  "stockholm",
  "brussels"
]


#iterate over each question and its corresponding answers from list of 10 european countries and their capital
for i in range(len(Countries_with_capitals)):

#Asking questions to  user
 user_input = input(Countries_with_capitals[i] + " ")

# The responses from the user 
 if user_input.strip().lower() == right_answers[i]:
  print("The answer is correct!")

 else:
     print(f"The answer is wrong.The correct answer is {right_answers[i].capitalize()}.")