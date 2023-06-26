from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question = item['question']
    answer = item['correct_answer']
    new_question = Question(question,answer)
    question_bank.append(new_question)

quizbrain = QuizBrain(question_bank)

while quizbrain.still_has_questions():
    quizbrain.next_question()

print("Congrats on completing the quiz")
print(f"Your final score is {quizbrain.score}/{quizbrain.question_number}\n")