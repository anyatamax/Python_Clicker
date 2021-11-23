from tkinter import Tk, Canvas, PhotoImage, Label
import ClickerClass


def main():
    root = Tk()
    root.title('Clicker')
    root.geometry("1000x714")

    C = Canvas(root, bg="white", height=0, width=0)
    filename = PhotoImage(file="Клик4.gif")
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.pack()

    app = ClickerClass.Clicker(root)
    app.pack()
    root.bind("<space>", lambda event=None: app.btn1.invoke())
    root.mainloop()


if __name__ == '__main__':
    main()
