import tkinter as tk


class Quiz:
    score = 0

    def __init__(self, answer, window):
        self.start = 0
        self.answer = ''
        # self.button_true = tk.Button(window, text='TRUE', command=lambda: answer.set('True'), bg='#ffc93c', font=('arial', 30, 'bold'))
        # self.button_false = tk.Button(window, text='FALSE', command=lambda: answer.set('False'), bg='#ffc93c', font=('arial', 30, 'bold'))

    def button_true_clicked(self):
        self.answer = "True"

    def button_false_clicked(self):
        self.answer = "False"

    def check(self, answer, correct_answer):
        if answer == correct_answer:
            self.score += 1

    def next(self):
        self.start += 1

    # def place(self):
    #     self.button_true.place(x=50, y=400)
    #     self.button_false.place(x=587, y=400)
