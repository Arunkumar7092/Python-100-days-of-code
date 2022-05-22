from data import question_data
from question import Question
from quizz import Quizz
from quizz_ui import QuizInterface

final = []
for each in question_data:
    text = each["question"]
    answer = each["correct_answer"]
    obj = Question(text, answer)
    final.append(obj)

quizz = Quizz(final)
quizz_ui = QuizInterface(quizz)






