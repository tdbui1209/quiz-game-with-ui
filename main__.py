from ui import UI
import tkinter as tk
from data import data
# from get_question import data
from quiz import Quiz
import random

random.shuffle(data)
window = tk.Tk()
window.title('True Or False')
window.minsize(width=800, height=600)
window.maxsize(width=800, height=600)
answer = tk.StringVar()

ui = UI()
quiz = Quiz(answer, window)


def check(answer, key):
    if answer == key:
        ui.a.itemconfig(ui.text, text='CORRECT', fill='#81b214')
    else:
        ui.a.itemconfig(ui.text, text='WRONG', fill='#ce1212')


def run(i):
    ui.show_question(data[i]['question'], i + 1)
    ui.pack()
    button_true = tk.Button(window, text='TRUE', command=lambda: answer.set('True'), bg='#ffc93c', font=('arial', 30, 'bold'))
    button_false = tk.Button(window, text='FALSE', command=lambda: answer.set('False'), bg='#ffc93c', font=('arial', 30, 'bold'))
    button_true.place(x=50, y=400)
    button_false.place(x=587, y=400)
    window.wait_variable(answer)
    check(answer.get(), data[i]['correct_answer'])
    # print(answer.get(), data[i]['correct_answer'])
    if i < len(data)-1:
        window.after(0, run, i+1)


run(0)

ui.pack()

window.mainloop()
