from quiz.quiz_game import QuizGame
from quiz.question import Question

# Sample questions
question1 = Question("What is the capital of France?",
                     ["A) London", "B) Paris", "C) Rome", "D) Madrid"],
                     "B")
question2 = Question("Which planet is known as the Red Planet?",
                     ["A) Jupiter", "B) Mars", "C) Saturn", "D) Neptune"],
                     "B")
question3 = Question("Who painted the Mona Lisa?",
                     ["A) Michelangelo", "B) Leonardo da Vinci", "C) Vincent van Gogh", "D) Pablo Picasso"],
                     "B")

# Create a quiz game instance
quiz = QuizGame([question1, question2, question3])

# Play the quiz
quiz.play()