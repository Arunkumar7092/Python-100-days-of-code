from data import question_data
from question_model import Question
from quiz_brain import Quizz


final = []
for question in question_data:
    text = question["text"]
    answer = question["answer"]
    obj = Question(text, answer)
    final.append(obj)

quizz_obj = Quizz(final)

while quizz_obj.run_till():    
    quizz_obj.display_question()
print("You are completed the Quizz")
print(f"Your final score is {quizz_obj.score}/{quizz_obj.question_number}")