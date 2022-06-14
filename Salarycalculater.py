import tkinter as tk
from tkinter import messagebox as msgbox

def calculate(stundenlohn, worktime, monat):
    tag = float(stundenlohn) * float(worktime)
    mon = tag * float(monat)
    year = mon * 12
    text = f"Am Tag verdienst du {tag} €.\nIn einem Monat verdienst du {mon} €.\nIm Jahr verdienst du {year} €."
    msgbox.showinfo("Gehalt", text)


def ok():
    msg = tk.Tk()
    msg.geometry("450x250")
    msg.title("Gehaltsrechner")
    but3 = tk.Button(msg, text="Zurück",
                     command=msg.destroy,
                     bg="blue"); but3.grid(row=6, column=3)
    lab2 = tk.Label(msg, text="Rechne hier deinen Gehalt aus",
                    fg="#00ff00",
                    bg="green"); lab2.grid(row=0)

    lab3 = tk.Label(master=msg, text="Gebe hier deinen Stundenlohn an:"); lab3.grid(row=1)
    lab4 = tk.Label(master=msg, text="Gebe hier deine Arbeitszeit pro Tag an:"); lab4.grid(row=2)
    lab5 = tk.Label(master=msg, text="Gebe hier deine Arbeitstage pro Monat an:"); lab5.grid(row=3)
    lab_credits = tk.Label(master=msg, text="Erstellt von Dennis Makus"); lab_credits.grid(row=4)

    entry_num1 = tk.Entry(master=msg); entry_num1.grid(row=1, column=1)
    entry_num2 = tk.Entry(master=msg); entry_num2.grid(row=2, column=1)
    entry_num3 = tk.Entry(master=msg); entry_num3.grid(row=3, column=1)

    button_calc = tk.Button(master=msg, text="Gehalt berechnen", command=lambda: calculate(entry_num1.get(),
    entry_num2.get(), entry_num3.get())).grid(row=5, column=1)

    msg.mainloop()

def close():
    window.destroy()


window = tk.Tk()
window.geometry("500x500")
window.title("Herzlich Willkommen")
lab1 = tk.Label(window, text="Danke für das Benutzen der App",
                fg='#00ff00',
                bg="green",
                height=3, width=24)
but1 = tk.Button(window, text="Weiter zum Rechner", command=ok,
                 fg="#00ff00",
                 bg="red",
                 height=5, width=15)
but2 = tk.Button(window, text="Schließen", command=close,
                 bg="blue",
                 height=5, width=15)

lab1.pack()
but1.pack()
but2.pack()

window.mainloop()