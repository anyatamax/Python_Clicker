from tkinter import Label, Button
import tkinter as tk


class CountClick:
    click_count = 0
    click_amount = 1
    click_cost = 5


class Clicker(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs, bg="#fff")
        self.parent = parent

        self.label_1 = Label(self, text=str(CountClick.click_count), font=('Helvetica 100'), bg="#fff")
        self.label_1.pack()

        self.space_1 = Label(self, text='', font=('Arial 20'), bg="#fff")
        self.space_1.pack()

        self.label_2 = Label(self, text='Every click: ' + str(CountClick.click_amount), font=('Arial 30'), bg="#fff")
        self.label_2.pack()

        self.label_3 = Label(self, text='Cost of update: ' + str(CountClick.click_cost), font=('Arial 30'), bg="#fff")
        self.label_3.pack()

        self.space_4 = Label(self, text='', font=('Arial 30'), bg="#fff")
        self.space_4.pack()

        self.btn1 = Button(self, text="Click", background="#800", foreground="#fff", font="Arial 50", command=self.up_click_count)
        self.btn1.pack()

        self.btn3 = Button(self, text="Update", background="#000", foreground="#fff", padx="60", pady="10", font="Arial 60"
                      , command=self.bonus_click_count)
        self.btn3.pack()


        self.btn2 = Button(self, text="Reset", background="#800", foreground="#fff", padx="20", pady="8", font="Arial 50"
                      , command=self.reset_click_count)
        self.btn2.pack()

    def bonus_click_count(self):
        if CountClick.click_count >= CountClick.click_cost:
            CountClick.click_count = CountClick.click_count - CountClick.click_cost
            CountClick.click_amount = CountClick.click_amount * 2
            CountClick.click_cost = CountClick.click_cost + 100
        self.label_1['text'] = str(CountClick.click_count)
        self.label_2['text'] = 'Every click: ' + str(CountClick.click_amount)
        self.label_3['text'] = 'Cost of update: ' + str(CountClick.click_cost)

    def up_click_count(self):
        CountClick.click_count = CountClick.click_count + CountClick.click_amount
        self.label_1['text'] = str(CountClick.click_count)

    def reset_click_count(self):
        CountClick.click_count = 0
        CountClick.click_amount = 1
        CountClick.click_cost = 5
        self.label_1['text'] = str(CountClick.click_count)
        self.label_2['text'] = 'Every click: ' + str(CountClick.click_amount)
        self.label_3['text'] = 'Cost of update: ' + str(CountClick.click_cost)