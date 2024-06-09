import json

with open("files/questions.json", "r") as file:
    content = file.read()

data = json.loads(content)

for question in data:
    print(question['question'])
    for index, alternative in enumerate(question['alternatives']):
        print(index + 1, "-", alternative)
    userChoice = int(input("Enter your answer: "))
    question["userChoice"] = userChoice

score = 0
for index, question in enumerate(data):
    if question["userChoice"] == question["correctAnswer"]:
        score = score + 1
        result = "Correct answer!"
    else:
        result = "Wrong answer!"
    message = (f"{result} for Question {index + 1}, Your answer: {question['userChoice']}, "
               f"Correct answer: {question['correctAnswer']}")
    print(message)

print(str(score) + "/" + str(len(data)))
