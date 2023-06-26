class QuizBrain:

    def __init__ (self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score =0 

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
          

    def next_question(self):
        self.question_number+=1
        current_question = self.question_list[self.question_number]
        choice = input(f"Q.{self.question_number } : {current_question.text} (true/false) : ")
        self.check_answer(choice, current_question.answer)

    def check_answer(self,choice,current_question):
        if choice.lower() == current_question.lower():
            print("You got it right mate")
            self.score+=1
            print(f"Your score is {self.score}/{self.question_number} ")

        else :
            print("Wrong answer  :/ \n")

