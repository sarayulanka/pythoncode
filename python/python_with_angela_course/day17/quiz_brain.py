
class QuizBrain:
    
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 1

    
    def next_question(self):
        score = 0

        while self.question_number <= 10:
            user_answer = input(f"{self.question_list[self.question_number]['text']} True / False:  ").lower()
            if user_answer == self.question_list[self.question_number]["answer"].lower():
                score += 1
                print(f"That's right! Score: {score}/{self.question_number}")
                self.question_number += 1
            else:
                print("That's wrong.")
                print(f"Correct answer: {self.question_list[self.question_number]['answer']}")
                print(f"Score: {score}/{self.question_number}")
                self.question_number += 1

        print(f"Final score: {score}/10. ")