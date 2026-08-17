class QuizBrain:

    def __init__(self,questions_list):
        self.questions = questions_list
        self.questionNumber = 0
        self.score = 0

    def still_has_questions(self):
        return self.questionNumber < len(self.questions)

    def next_question(self):
        q = self.questions[self.questionNumber]
        self.questionNumber += 1
        user_answer = input(f"Q{self.questionNumber}:{q.text} (T for 'True' F for 'False'): ")
        self.check_answer(user_answer,q.answer)


    def check_answer(self,user_answer,true_answer):

        if user_answer.lower() == true_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect!")
        if true_answer == "t":
            true_answer = "True"
        else:
            true_answer = "False"
        print("The correct answer was: " + true_answer)
        print(f"your current score is: {self.score}/{self.questionNumber}\n")










