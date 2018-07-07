from tkinter import *


class Program:

    buttons = []

    def __init__(self, master, contents):
        frame = LabelFrame(master, text="Program")
        frame.pack(side=TOP, anchor=W, padx=2)

        # pinched from https://stackoverflow.com/a/16198198
        scroll_bar = Scrollbar(frame, orient=HORIZONTAL)
        scroll_bar.pack(fill=X, side=BOTTOM, expand=FALSE)
        canvas = Canvas(frame, bd=0, highlightthickness=0, height=50,
                        xscrollcommand=scroll_bar.set)
        canvas.pack(side=BOTTOM, fill=BOTH, expand=TRUE)
        scroll_bar.config(command=canvas.xview)

        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor=NW)

        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())
        interior.bind('<Configure>', _configure_interior)


        for c in contents:
            b = Button(self.interior, width=2, pady=5, text=c, font='TkFixedFont 20')
            b.pack(side=LEFT)
