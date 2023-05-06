from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT_SIZE = 20
FONT_EFFECT = "italic"
FONT_NAME = "Comic Sans"
FONT = (FONT_NAME, FONT_SIZE, FONT_EFFECT)


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Some question text", font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.label_score = Label(text=f"Score: {self.quiz.score}", fg='white', bg=THEME_COLOR)
        self.label_score.grid(row=0, column=1)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_chosen)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_chosen)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.label_score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_chosen(self):
        is_right = self.quiz.check_answer("True")
        print(f"True was chosen -- {is_right}")
        self.give_feedback(is_right)

    def false_chosen(self):
        is_right = self.quiz.check_answer("False")
        print(f"False was chosen -- {is_right}")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            print("trying to change to green")
            self.canvas.config(bg="green")
        else:
            print("trying to change to red")
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def reset_color(self):
        self.canvas.config(bg="white")
