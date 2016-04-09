import hashlib
import os
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror, showinfo


def md5(filename):
    summator = hashlib.md5()
    with open(filename, 'rb') as f:
        while True:
            t = f.read(1024)
            if not t:
                break
            summator.update(t)
    return summator.hexdigest()


class Container:
    def __init__(self):
        self.root = Tk()

        self.filename = StringVar(self.root)
        self.e_dirc = Entry(self.root,
                            textvariable=self.filename,
                            width=80)
        self.e_dirc.grid(row=0, column=0, sticky=NSEW)

        self.pattern = StringVar(self.root)
        self.e_pattern = Entry(self.root,
                               textvariable=self.pattern,
                               width=80)
        self.e_pattern.grid(row=1, column=0, sticky=NSEW)

        self.l_show = Label(self.root,
                            width=80)
        self.l_show.grid(row=2, column=0, sticky=NSEW)

        self.b_open = Button(self.root,
                             text="Open",
                             command=self.f_open,
                             width=10)
        self.b_open.grid(row=0, column=1, sticky=S+N+E)

        self.b_clear = Button(self.root,
                              text="Clear",
                              command=self.f_clear,
                              width=10)
        self.b_clear.grid(row=1, column=1, sticky=S+N+E)

        self.b_copy = Button(self.root,
                             text="Copy",
                             command=self.f_copy,
                             width=10)
        self.b_copy.grid(row=2, column=1, sticky=S+N+E)

        self.b_calc = Button(self.root,
                             text="Go!",
                             command=self.f_calc,
                             width=10)
        self.b_calc.grid(row=3, column=1, sticky=S+N+E)

        self.b_verify = Button(self.root,
                               text="Verify",
                               command=self.f_verify,
                               width=10)
        self.b_verify.grid(row=3, column=0, sticky=S+N+E)

        self.result = ''

    def f_open(self):
        self.l_show.config(text='')
        self.result = ''
        filename = askopenfilename(master=self.root)
        if filename:
            self.filename.set(filename)

    def f_clear(self):
        self.pattern.set('')

    def f_calc(self):
        filename = self.filename.get()
        if os.path.exists(filename):
            res = md5(filename)
            self.l_show.config(text=res)
            self.result = res

    def f_copy(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.result)

    def f_verify(self):
        pattern = self.pattern.get()
        if self.result and pattern:
            if self.result == pattern:
                showinfo(message="Hash is correct!")
            else:
                showerror(message="Hash is incorrect!")


if __name__ == '__main__':
    interface = Container()
    interface.root.mainloop()