from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

questionBank = []
for question in question_data:
    questionBank.append(Question(question["text"],question["answer"]))


quiz = QuizBrain(questionBank)

while quiz.still_has_questions():
    quiz.next_question()
print(f"Congratulations! you completed the quiz.\nyour final score is {quiz.score}/{quiz.questionNumber}.")

