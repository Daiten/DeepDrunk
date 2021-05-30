import tkinter as tk
from random_script_dd import *
import webbrowser


def callback(url):
    webbrowser.open_new(url)


class NewprojectApp:


    def message_write(self):
        cocktail_generate_print_to_window()
        self.label1.configure(self.toplevel1, text=cocktail_generate_print_to_window())





    def __init__(self, master=None):
        # build ui
        self.toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        self.toplevel1.wm_title("Deep Drunk")
        self.frame1 = tk.Frame(self.toplevel1)

        self.label1 = tk.Label(self.frame1, font=("Courier", 18))
        self.label1.configure(height='15', width='30', fg='white', bg='black')
        self.label1.pack(side='top')
        self.button1 = tk.Button(self.frame1, command=self.message_write, height='5', width='30', font=("Courier", 18))
        self.button1.configure(text='Generate', fg='white', bg='black')
        self.button1.pack(side='top')
        self.button2 = tk.Button(self.frame1, command=self.message_write_iba, height='5', width='30', font=("Courier", 18))
        self.button2.configure(text='Generate IBA', fg='white', bg='black')
        self.button2.pack(side='top')
        self.frame1.configure(height='600', width='600')
        self.frame1.pack(side='top')
        self.toplevel1.configure(height='600', width='600')



        # Main widget
        self.mainwindow = self.toplevel1


    def message_write_iba(self):
        unit = iba_cocktail_generate_print_to_window()
        self.label1.configure(text=unit, cursor="hand2")
        self.label1.pack()
        self.label1.bind("<Button-1>", lambda e: callback("https://en.wikipedia.org/wiki/" + str(unit).replace(" ",
                                                                                                               "_")))





    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    app = NewprojectApp()
    app.run()

