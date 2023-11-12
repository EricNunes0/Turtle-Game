from tkinter import Tk, ttk
from settings import screen_title

def create_popup(screen, message: str | None):
    popup = Tk()
    popup.wm_title(screen_title)
    label = ttk.Label(popup, text=message, font=("Arial", 10, "bold"))
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Ok", command = lambda: destroy_popup(screen=screen, popup=popup))
    B1.pack()
    popup.mainloop()

def destroy_popup(screen, popup):
    try:
        popup.destroy()
        screen.bye()
    except Exception as e:
        print(e)