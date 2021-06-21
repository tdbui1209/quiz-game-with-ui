import tkinter as tk


class UI:

    def __init__(self):
        self.a = tk.Canvas(width=800, height=600, bg='#dbf6e9')
        self.a.create_rectangle(60, 40, 760, 310, fill='#000000')
        self.a.create_rectangle(60, 410, 203, 490, fill='#000000')
        self.a.create_rectangle(597, 410, 760, 490, fill='#000000')
        self.a.create_rectangle(50, 30, 750, 300, fill='#ffc93c')
        self.disp_question = self.a.create_text(100, 80, text="question", fill='#000000', font=('Arial', 15, 'bold'), anchor='w', justify='left', width=600)
        self.text = self.a.create_text(400, 400, text='', font=('Arial', 30, 'bold'), anchor='c', width=600)

    def show_question(self, question, i):
        self.a.itemconfig(self.disp_question, text=f'Q{i}. {question}')

    def check(self, answer, key):
        if answer == key:
            self.a.create_text(400, 400, text='CORRECT', fill='#81b214', font=('Arial', 30, 'bold'), anchor='c', width=600)
        else:
            self.a.create_text(400, 400, text='WRONG', fill='#ce1212', font=('Arial', 30, 'bold'), anchor='c', width=600)

    def pack(self):
        self.a.pack()
