import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # self.hi_there = tk.Button(self)
        # self.hi_there["text"] = "Hello World\n(click me)"
        # self.hi_there["command"] = self.say_hi
        # self.hi_there.pack(side="top")
        #
        # self.quit = tk.Button(self, text="QUIT", fg="red",
        #                       command=self.master.destroy)
        # self.quit.pack(side="bottom")
        self.bt1=tk.Button(self,bg="black",padx=20)
        self.bt1.grid(row=0, column=1)

        self.bt2 = tk.Button(self, bg="blue")
        self.bt2.grid(row=0, column=2)

        self.bt3 = tk.Button(self, bg="black")
        self.bt3.grid(row=0, column=3)

        self.bt4 = tk.Button(self, bg="black")
        self.bt4.grid(row=1, column=1)

        self.bt5 = tk.Button(self, bg="black")
        self.bt5.grid(row=1, column=2)

        self.bt6 = tk.Button(self, bg="black")
        self.bt6.grid(row=1, column=3)

        self.bt6 = tk.Button(self, bg="black")
        self.bt6.grid(row=2, column=1)

        self.bt6 = tk.Button(self, bg="black")
        self.bt6.grid(row=2, column=2)

        self.bt6 = tk.Button(self, bg="black")
        self.bt6.grid(row=2, column=3)






    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
