# This entrypoint file to be used in development. Start by reading README.md
# from unittest import main
import prob_calculator
from tkinter import *
from tkinter import ttk


def click_add_button():
    user_hat.add_color_ball(color.get(), amount.get())
    print(user_hat)


# So, now we are going to create a small interface so that a user can continue to run these simulations
# as long as they see fit. For that, we are going to use tkinter.
# 1. We have to create the environment for the user, they need an empty hat to add balls into.
# 2. We had to create an "add_color_ball" function to the hat class because the interface functions differently
# from the way the test_module uses it. We have to give the user the ability to add ass many colors they want to
# the hat.
user_hat = prob_calculator.Hat()

# 3. Now we have to create the interface using tkinter.
# We initialize the window and set a title.
root = Tk()
root.title("Probability Calculator")
root.geometry("350x300")

# We create a frame for our window to use the newer ttk code
# . This can be one of: flat (default), raised, sunken, solid, ridge, or groove.
add_to_hat_frame = ttk.Frame(root, borderwidth=4, relief="ridge", padding=5)
add_to_hat_frame.grid(column=0, row=0)

# This is the title label inside of my frame for adding balls into the hat.
# We put it into the top left corner of the program.
title_label = ttk.Label(add_to_hat_frame, text="Choose a color and add whatever amount you want!")
title_label.grid(row=0, column=0, columnspan=2)

# We need to create the entry field for adding items into our interface as well as the add button.
# We add them to the grid immediately. After each creation and addition to the grid, I will make a label to the
# input boxes so it is clear what the user has to enter.

# This will be a string entry and will only accept string. We will write that in a different function.
color = StringVar()
color.set("Red")
color_to_add = ttk.Combobox(add_to_hat_frame, textvariable=color, state="readonly", width=10,
                            values=("Red", "Blue", "Green", "Yellow", "Pink", "White", "Black", "Brown", "Grey",
                                    "Purple", "Orange", "Silver", "Violet", "Gold",)).grid(row=1, column=0)
# color_to_add.bind('<<ComboboxSelected>>', function)
color_label = ttk.Label(add_to_hat_frame, text="Color of Ball").grid(row=1, column=1)

# This will be a integer entry, and will accept any number.
# Later I will add a limit.
amount = IntVar()
amount_to_add = ttk.Entry(add_to_hat_frame, textvariable=amount, width=10).grid(row=2, column=0)
amount_label = ttk.Label(add_to_hat_frame, text="Amount to Add").grid(row=2, column=1)

# And this is the final widget inside of this frame. It is an add button that takes the entry from both inputs and
# sends it to the Hat class's function to add contents to the hat.
add_button = ttk.Button(add_to_hat_frame, text="Add", command=lambda: click_add_button()).grid(row=3, column=0,
                                                                                               columnspan=2)

root.mainloop()

# Old code that came with the assignment.
"""
Run unit tests automatically, Came with assignment
main(module='test_module', exit=False)
hat = prob_calculator.Hat(blue=4, red=2, green=6)
probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)"""
