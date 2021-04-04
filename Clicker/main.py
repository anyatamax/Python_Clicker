from tkinter import *

tk = Tk()
tk.title('Clicker')
tk.geometry("1000x800")


C = Canvas(tk, bg="white", height=0, width=0)
filename = PhotoImage(file="Клик.gif")
background_label = Label(tk, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()

click_count = 0
click_amount = 1
click_cost = 5


def up_click_count():
    global click_count
    click_count = click_count + click_amount
    label_1['text'] = str(click_count)


def reset_click_count():
    global click_count
    global click_amount
    global click_cost
    click_count = 0
    click_amount = 1
    click_cost = 5
    label_1['text'] = str(click_count)
    label_2['text'] = 'Every click: ' + str(click_amount)
    label_3['text'] = 'Cost of update: ' + str(click_cost)


def bonus_click_count():
    global click_count
    global click_amount
    global click_cost
    if click_count >= click_cost:
        click_count = click_count - click_cost
        click_amount = click_amount * 2
        click_cost = click_cost + 100
    label_1['text'] = str(click_count)
    label_2['text'] = 'Every click: ' + str(click_amount)
    label_3['text'] = 'Cost of update: ' + str(click_cost)


label_1 = Label(tk, text=str(click_count), font=('Helvetica 100'), bg="#fff")
label_1.pack()

space_1 = Label(tk, text='', font=('Arial 20'), bg="#fff")
space_1.pack()

label_2 = Label(tk, text='Every click: ' + str(click_amount), font=('Arial 30'), bg="#fff")
label_2.pack()

label_3 = Label(tk, text='Cost of update: ' + str(click_cost), font=('Arial 30'), bg="#fff")
label_3.pack()

space_4 = Label(tk, text='', font=('Arial 30'), bg="#fff")
space_4.pack()

btn1 = Button(tk, text="Click", background="#800", foreground="#fff", font="Arial 50", command=up_click_count)
btn1.place(x=340, y=320)

btn3 = Button(tk, text="Update", background="#000", foreground="#fff", padx="60", pady="10", font="Arial 60"
              , command=bonus_click_count)
btn3.place(x=130, y=450)

btn2 = Button(tk, text="Reset", background="#800", foreground="#fff", padx="20", pady="8", font="Arial 50"
              , command=reset_click_count)
btn2.place(x=300, y=600)

tk.bind("<space>", lambda event=None: btn1.invoke())

mainloop()
