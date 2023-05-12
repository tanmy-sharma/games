import requests
import json

# Make an API call to the Open Trivia Database
url = "https://opentdb.com/api.php?amount=50&category=22"
response = requests.get(url)
data = json.loads(response.text)

# Extract the questions from the API response
questions = data["results"]

#Work Through Each Question
correct_answers = 0
for question in questions:
    print(question["question"])
    print("Options:")
    for i in range(len(question["incorrect_answers"])):
        print(f"{i+1}. {question['incorrect_answers'][i]}")
    print(f"{len(question['incorrect_answers'])+1}. {question['correct_answer']}")
    user_answer = int(input("Enter the number of your answer: "))
    if user_answer == len(question["incorrect_answers"]) + 1:
        print("Correct!")
        correct_answers += 1
    else:
        print("Incorrect.")

# Print the final score
print(f"You got {correct_answers} out of {len(questions)} questions correct.")
