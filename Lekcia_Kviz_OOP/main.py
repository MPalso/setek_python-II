from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_list = []

for one_question in question_data:
    question_t = one_question["text"]
    question_a = one_question["answer"]
    new_question = Question(question_t, question_a)
    question_list.append(new_question)

quiz = QuizBrain(question_list)
while quiz.has_question() == True:
    quiz.next_question()
print("Dokocili ste kviz")
print(f"Vase celove skore je: {quiz.score} / {quiz.question_number}")







