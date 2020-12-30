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

# This is the frame for the next part of the program. This part requires the user to create a list of what they expect
# the outcome of the random draw should be. The list will be continually updated and displayed on the right hand side
# in a new frame. I need to learn how to make my frames the same size to make it look better, or maybe get rid of the
# visual part of the frames and add these steps, that the user must do to make the program run, into a continuously
# updating frame, where the user hits a "next" button and the screen changes and you're on to the next step,




"""
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)
"""

# We need to move this code around because its making it hard for me to move see where certain things are. I need to
# group by categories such as, creation of widgets, adding them to the grid and so on. More on the comments ahead.

# This is variable creation for the widgets "textvariables" and other actions
color = StringVar().set("Red")  # for color_to_add widget
amount = IntVar()  # for amount_to_add widget
color_list = ["Red", "Blue", "Green", "Yellow", "Pink", "White", "Black", "Brown", "Grey", "Purple", "Orange",
              "Silver", "Violet", "Gold"]

# Here we will have all the widgets being created for the program. I need to keep these seperate in case I need to
# change any of the parameters for the widgets.
# This holds the first set of options that we give the user. It is to hold all the widgets pertaining to adding items to
# the hat object.
add_to_hat_frame = ttk.Frame(root, borderwidth=4, relief="ridge", padding=5)
# This label gives the user the instructions for the first frame.
instructions_one = ttk.Label(add_to_hat_frame, text="Choose a color for the ball.\n Add any amount you want.\n Hit the "
                                                    "ADD button to add the ball(s) to the hat!")
# This is the dropdown menu with the list of colors that the user may add. I did this so I didn't have to deal with
# string inputs. Might reduce number of  balls as it is just a small program and the list is large as it is
color_to_add = ttk.Combobox(add_to_hat_frame, textvariable=color, state="readonly", width=10, values=color_list)
# A label to go alongside the dropdown menu that we created above.
color_label = ttk.Label(add_to_hat_frame, text="Color of Ball")
# This will be a integer entry by the user. Will be used to add items to the hat. Will add limit later.
amount_to_add = ttk.Entry(add_to_hat_frame, textvariable=amount, width=10)
# A label to go alongside the "amount" entry widget that we created above.
amount_label = ttk.Label(add_to_hat_frame, text="Amount to Add")
# Our add button that confirms the users addition to the hat. Will call on click_to_add function created above.
add_button = ttk.Button(add_to_hat_frame, text="Add", command=lambda: click_add_button())
# This is our next frame that hold our second set of instructions
what_to_draw_frame = ttk.Frame(root, borderwidth=4, relief="ridge", padding=5)
# The second set of instructions.
draw_label = ttk.Label(what_to_draw_frame, text="Which color of balls do you expect to be drawn?\nThe drawing list "
                                                "is updated on the side ==>")


# This is where all the variables will be added to the grid. Any further grid configuration for the widgets will
# probably put here as well unless they become a nuisance and I place that code elsewhere.
add_to_hat_frame.grid(column=0, row=0)
instructions_one.grid(row=0, column=0, columnspan=2)
color_to_add.grid(row=1, column=0)
color_label.grid(row=1, column=1)
amount_to_add.grid(row=2, column=0)
amount_label.grid(row=2, column=1)
add_button.grid(row=3, column=0, columnspan=2)


what_to_draw_frame.grid(row=1, column=0, columnspan=2)
draw_label.grid(row=0, column=0, columnspan=2)


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
