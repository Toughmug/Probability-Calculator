import copy
import random


class Hat:
    def __init__(self, **kwargs):
        # So we need to create a list of strings for each the 'Hat' object. It is named 'contents' and in it,
        # are a variable number of ball colors, as determined when the object is created by the user. For example,
        # is we call Hat(red=2, yellow=1), we will get a list of ['red', 'red', 'yellow']. We do this by passing
        # in **kwargs into out init, since we never know how many are going to be added by the user. Next, we loop
        # through the **kwargs, but grabbing both the 'color'(as a string) and the amount of each of those colors.
        # Then we make a small loop with inside that loop that will run for the amount of times each color is needed.
        # While in that inner loop, we keep adding the color as a string into our 'contents' list.
        self.contents = list()
        for color, amount in kwargs.items():
            for i in range(amount):
                self.contents.append(color)

    def draw(self, draw_amount):
        balls_drawn = list()
        length = len(self.contents) - 1

        # This if-else statement is used to check to see if the draw_amount is equal to or greater than
        # the length of the contents in the hat. If it is, we return a copy of the contents list, if not
        # then we continue with actually drawing a certain amount.
        if draw_amount >= length + 1:
            return copy.deepcopy(self.contents)

        # This is the loop to keep drawing. It draws as entered when the function was called.
        # We need to get a random number between 0 and the length of the 'self.contents' minus "i", "i" being
        # the iterator used to loop through amount of balls needed. That is so we don't go out of the index because
        # we keep making the contents smaller by one every time we draw. We use the imported "random" module.
        for i in range(draw_amount):
            random_number = random.randint(0, (length - i))
            balls_drawn.append(self.contents.pop(random_number))
        return balls_drawn


def create_drawn_dict(list_of_balls):
    # This function is used to create a dictionary from the list of the balls that were drawn form the
    # hat in the experiment function. We create a dictionary to make it easy to compare to further in
    # the experiment. A simple for loop to iterate over the list and then an if-else statement to increment
    # the counts in our dictionary.
    balls_dict = dict()
    for ball in list_of_balls:
        if ball in balls_dict:
            balls_dict[ball] += 1
        else:
            balls_dict[ball] = 1
    return balls_dict


def check_balls_drawn(expected, drawn_balls):
    # This function is used to check if the balls expected in our experiment are in the balls that were drawn.
    # We return False if the "color of ball" expected is not in the "drawn balls" dictionary. It also returns
    # false if the "color of drawn balls" is not equal to or greater than that expected. The True and False are
    # used to increment a count loop in the experiment() function.
    for color, amount_expected in expected.items():
        if color not in drawn_balls:
            return False
        if drawn_balls[color] >= amount_expected:
            continue
        else:
            return False
    return True


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    total_count = 0  # The number of times the correct amount of expected_balls were found in the balls that were drawn.

    # This for loop is go through the number of experiments passed into the function. In the loop, we make a copy of
    # the hat and then we draw the balls from that copy. We have to make a copy as everytime that we draw from the hat,
    # the contents of the hat decrease. To run the experiments many times, we need alter the contents of a copy rather
    # than the original. After getting the list of balls drawn, we make that list into a dictionary with key="color"
    # and value="number of times drawn". We do this for our next if statement to easily check if the colors of drawn
    # balls match what was expected for the experiment. We delete the copy of the hat to save memory and start the
    # next loop/experiment.
    for i in range(num_experiments):
        cpy_of_hat = copy.deepcopy(hat)
        balls_drawn = cpy_of_hat.draw(num_balls_drawn)
        ball_dict = create_drawn_dict(balls_drawn)

        if check_balls_drawn(expected_balls, ball_dict) is True:
            total_count += 1
        del cpy_of_hat

    # To get the Probability, we use the "total_count", which is the number of times the drawn_balls matched what was
    # expected in the experiment, and divide by the number of experiments made. We return that value and the experiment
    # is done.
    probability = total_count / num_experiments
    return probability
