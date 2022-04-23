class Quizz:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
    
    def display_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        correct_answer = current_question.answer
        self.check_answer(user_answer, correct_answer)
    
    def run_till(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got the correct answer")
            self.score += 1
        else:
            print("Your answer is wrong")
        print(f"The correct answer is {correct_answer} ")
        print(f"your score is {self.score}/{self.question_number}")
        