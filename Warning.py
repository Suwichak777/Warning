import tkinter as tk

def Yes1():
    global win2
    win1.withdraw()

    win2 = tk.Toplevel()
    win2.title("Warning!")
    win2.geometry("500x350")
    warn_con = tk.Label(win2, text="You sure?", font=("Arial", 50), fg="red")
    warn_con.pack(pady=50)

    but_frame = tk.Frame(win2)
    but_frame.pack(pady=20)

    button1 = tk.Button(but_frame, text="Yes", font=("Arial", 15), command=Yes2)
    button2 = tk.Button(but_frame, text=" No ", font=("Arial", 15))
    button1.pack(side=tk.LEFT, padx=10)
    button2.pack(side=tk.LEFT, padx=40)

def Yes2():
    win2.destroy()

    win3 = tk.Toplevel(win1)
    win3.title("Warning!")
    win3.geometry("500x350")
    warn_con = tk.Label(win3, text="Just kidding!", font=("Arial", 50), fg="green")
    warn_con.pack(pady=100)

    def close_all():
        win3.destroy()
        win1.destroy()

    win3.after(5000, close_all)

def No1():
    win1.withdraw()

    win4 = tk.Toplevel()
    win4.title("Warning!")
    win4.geometry("500x350")
    warn_con = tk.Label(win4, text="Operation cancelled", font=("Arial", 30), fg="blue")
    warn_con.pack(pady=100)

    def close_all():
        win4.destroy()
        win1.destroy()

    win4.after(5000, close_all)

win1 = tk.Tk()
win1.title("Warning!")
win1.geometry("500x350")

warning = tk.Label(win1, text="!!!Warning!!!", font=("Arial", 50), fg="red")
warning.pack(pady=20)
sure = tk.Label(win1, text="Are you sure to continue?", font=("Arial", 20))
sure.pack(pady=20)

but_frame = tk.Frame(win1)
but_frame.pack(pady=20)

button1 = tk.Button(but_frame, text="Yes", font=("Arial", 15), command=Yes1)
button2 = tk.Button(but_frame, text=" No ", font=("Arial", 15), command=No1)
button1.pack(side=tk.LEFT, padx=10)
button2.pack(side=tk.LEFT, padx=40)

win1.mainloop()