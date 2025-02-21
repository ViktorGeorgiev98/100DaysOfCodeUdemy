from question_model import Question
from data import question_data as questions
from quiz_brain import QuizBrain
question_bank = []

for question in questions:
    current_question = Question(question["text"], question["answer"])
    question_bank.append(current_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")