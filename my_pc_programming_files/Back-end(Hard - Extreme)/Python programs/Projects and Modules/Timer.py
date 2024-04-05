import tkinter as tk
import time
import threading
class MyGUI:
    def __init__(self):
        self._main = tk.Tk()
        self._main.title("TIMER!")
        self._main.geometry("1000x500")

        self._willRun = tk.BooleanVar()
        self._willRun = False
        self._Time = tk.StringVar()
        self._Time = "00:00:00"

        self._sec = tk.IntVar
        self._min = tk.IntVar
        self._hr = tk.IntVar

        self._sec = 0
        self._min = 0
        self._hr = 0

        self._TimeDisplay = tk.Label(self._main, font=("sans-serif", 180), text=self._Time)
        self._TimeDisplay.pack(pady=20)

        self._btn = tk.Button(self._main, font=("Arial", 26), text="Start", command=self.startORstop)
        self._btn.pack()

        self._main.mainloop()
    def startORstop(self):

        if self._willRun:
            self._willRun = False
            self._TimeDisplay.config(foreground="black")
            self._btn.config(text="Start")

        elif not self._willRun:
            self._willRun = True
            t1 = threading.Thread(target=self.TimerRun)
            t1.start()


    def TimerRun(self):
        sth = 0
        while self._willRun:

            if not self._willRun:
                pass

            elif self._willRun:
                self._sec += 1

                if self._sec >= 60:
                    self._sec -= 60
                    self._min += 1

                elif self._min >= 60:
                    self._min -= 60
                    self._hr += 1

                self._TimeDisplay.config(text=f"{self._hr}:{self._min}:{self._sec}", foreground="red")
                self._btn.config(text="Stop")
                #print(f"{self._hr}:{self._min}:{self._sec}")
            time.sleep(1)
MyGUI()