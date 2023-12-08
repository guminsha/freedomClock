from tkinter import *
from datetime import datetime


def update_timer():
    now_time = datetime.now()
    end_time = datetime(2023, 12, 16, 7, 0)  # 16 12 2023 07:00
    time_left = end_time - now_time
    list_time_left = convert_time(time_left)
    label_time.config(text=f"{list_time_left[0]} Dias"
                           f" {list_time_left[1]} Horas "
                           f"{list_time_left[2]} Minutos "
                           f"{list_time_left[3]} Segundos")
    label_time.after(1000, update_timer)


def convert_time(time):
    days = time.days
    hours, remaining = divmod(time.seconds, 3600)
    minutes, seconds = divmod(remaining, 60)
    return days, hours, minutes, seconds


window = Tk()

window.config(bg="black")

window.title("Relógio da Liberdade")
window.geometry("990x260")
# icon = PhotoImage(file=os.path.join("./assets/icon.png"))
# window.iconphoto(True, icon)
window.resizable(False, False)

label_title = Label(window,
                    text="TEMPORIZADOR DO LIVRAMENTO",
                    font=("Helvetica", 30),
                    bg="black",
                    fg="blue",
                    )
label_title.pack(pady=20)

label_time = Label(window,
                   font=("DS-Digital", 40),
                   bg="black",
                   fg="blue",
                   padx=20,
                   pady=10)
label_time.pack(anchor="center")

label_date = Label(window,
                   font=("Helvetica", 30),
                   bg="black",
                   fg="blue",
                   padx=20,
                   pady=10,
                   text="Sábado - 16/12/2023")
label_date.pack()

update_timer()

window.mainloop()
