from tkinter import *
from tkinter import ttk


class Interface:
    def __init__(self):
        self.root = Tk()
        self.root.title("Probability Calculator")
        self.root.geometry("350x300")

        # Some quick "bind" examples.
        """
        temp = ttk.Label(root, text="Starting...")
        temp.grid()
        temp.bind('<Enter>', lambda e: temp.configure(text='Moved mouse inside'))
        temp.bind('<Leave>', lambda e: temp.configure(text='Moved mouse outside'))
        temp.bind('<ButtonPress-1>', lambda e: temp.configure(text='Clicked left mouse button'))
        temp.bind('<3>', lambda e: temp.configure(text='Clicked right mouse button'))
        temp.bind('<Double-1>', lambda e: temp.configure(text='Double clicked'))
        temp.bind('<B3-Motion>', lambda e: temp.configure(text='right button drag to %d,%d' % (e.x, e.y)))
        """
        # Widget Introspection
        """def print_hierarchy(w, depth=0):
            print('  ' * depth + w.winfo_class() + ' w=' + str(w.winfo_width()) + ' h=' + str(
                w.winfo_height()) + ' x=' + str(w.winfo_x()) + ' y=' + str(w.winfo_y()))
            for i in w.winfo_children():
                print_hierarchy(i, depth + 1)

        print_hierarchy(root)"""
        # Available Events for binding
        """
        <Activate>:
            Window has become active.
            <Deactivate>:
            Window has been deactivated.
            <MouseWheel>:
            Scroll wheel on mouse has been moved.
            <KeyPress>:
            Key on keyboard has been pressed down.
            <KeyRelease>:
            Key has been released.
            <ButtonPress>:
            A mouse button has been pressed.
            <ButtonRelease>:
            A mouse button has been released.
            <Motion>:
            Mouse has been moved.
            <Configure>:
            Widget has changed size or position.
            <Destroy>:
            Widget is being destroyed.
            <FocusIn>:
            Widget has been given keyboard focus.
            <FocusOut>:
            Widget has lost keyboard focus.
            <Enter>:
            Mouse pointer enters widget.
            <Leave>:
            Mouse pointer leaves widget.
        """


        self.root.mainloop()


#class CreateWindow:
   # def __init__(self, ):"""

run_interface = Interface()
