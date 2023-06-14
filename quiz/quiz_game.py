import random
from utils.display import display_choices, display_final_score

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
    
    def play(self):
        random.shuffle(self.questions)
        for question in self.questions:
            print(question.question)
            display_choices(question.choices)
            user_answer = input("Enter your answer (A, B, C, or D): ")
            if user_answer.upper() == question.answer:
                self.score += 1
                print("Correct!")
            else:
                print("Incorrect!")
            print()
        display_final_score(self.score, len(self.questions))