from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank =[]

""" for i in range(len(question_data)):
    question_bank.append(Question(question_data[i]['text'], question_data[i]['answer'])) """


for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

#print(question_bank[2].text)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz!\nYour final score was: {quiz.score}/{quiz.question_number}")