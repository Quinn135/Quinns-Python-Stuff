import time
import tkinter as tk


def timer(timer_time, prinnt=None):
    tim1 = time.time()
    tim = 0
    while True:
        tim2 = time.time()
        if (tim2 - tim1) >= timer_time:
            break
        if prinnt:
            temptim = tim
            tim = round(tim2)
            if temptim != tim:
                print(tim - round(tim1), timer_time - (tim - round(tim1)))


window = tk.Tk()

words = tk.Label(text="Started", height=25, width=100)
button = tk.Button(text="Press to start timer",
                   command=lambda: timer(5, 1)
                   )
button.pack()
words.pack()
window.update()
words.pack()
window.update()

window.mainloop()
