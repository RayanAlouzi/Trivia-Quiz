class QuizBrain: 
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
       return self.question_number < len(self.question_list)
    
    def next_question(self):
        self.question_number += 1 
        current_question = self.question_list[self.question_number - 1]
        user_answer = input("Q." + str(self.question_number) + ": " + current_question.text + ": ")
        if user_answer.lower() == current_question.answer.lower():
            print("You got it right!")
            self.score += 1
    
    def return_score(self): 
        print(f"Your final score was: {self.score}/{self.question_number}")