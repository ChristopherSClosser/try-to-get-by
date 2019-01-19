"""GUI."""
from tkinter import Tk, Label, Frame
from threading import Timer
from intell.models import start, feed

MTX = start(9, 18)


class WindowFrame(Frame):
    """."""

    def __init__(self):
        """."""
        Frame.__init__(self)
        self.count = 0
        self.window = Tk()
        self.mtx = MTX
# window.configure(background='black')
# window['bg'] = 'black'
# window.geometry('500x500')
# window.title("BUGS!")
# COUNT = 0
# lbl = Label(
#     window,
#     text=('Hello'),
#     bg='black',
#     fg='white',
#     font=("Arial Bold", 50),
# )
# lbl.grid(column=0, row=0)
# import pdb; pdb.set_trace()


# def go_bugs(lbl=lbl, COUNT=COUNT):
#     """."""
#     lbl['text'] = (lbl['text'], COUNT)
#     # import pdb; pdb.set_trace()
#     COUNT = COUNT + 1
#     print(COUNT)
#     window.after(10, go_bugs)
    # threading.Timer(10, go_bugs())

# t = Timer(1, go_bugs)
# t.run()
# import pdb; pdb.set_trace()
# while True:



# import pdb; pdb.set_trace()
go_bugs()
window.mainloop()
