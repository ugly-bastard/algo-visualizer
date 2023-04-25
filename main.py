from pathFinding import path
from sorting import sort
from tkinter import Tk, Label, PhotoImage, ttk

def choice():
    ROWS = 50
    WIDTH = 500
    def algo(al, root):
        root.destroy()
        if al == "sort":
            sort.main()
        else:
            work = path.Working(ROWS,WIDTH)
            work.main()

    root=Tk()
    root.attributes('-type', 'dialog')
    root.geometry("300x200")
    # img = PhotoImage(file="Sorting.png")
    # img = img.subsample(5,5)
    # label = Label(root, image = img)
    # label.pack()
    ttk.Button(root, text="Path Finding", width=20,
               command = lambda: algo("path", root)
               ).pack(pady=20)
    ttk.Button(root, text="Sorting", width=20,
               command = lambda: algo("sort", root)
               ).pack(pady=20)
    root.mainloop()

if __name__ == "__main__":
    choice()
