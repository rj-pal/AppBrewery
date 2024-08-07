from tkinter import *
import PIL.Image
import PIL.ImageTk

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

timer = None
minute: int = 0
second: int = 0


def pomodoro(start_minute: int = 25, timer_type: str = 'timer'):
    """
    Pomodoro Timer Function contains code for the user interface built on Tkinter and all inner functions outside the
    main window loop that control button clicks and the working of the timer. It depends on three global parameters:
    a timer window (a delaying window function for running the timer), and a minute variable and a second variable
    (for keeping track of the time). It runs a simple timer with a default count down time of 25 minutes, and
    a default timer name of 'timer'. Both variables can be set by the user.
    """
    global minute

    # Validation for the minute variable as a float will still work but will ruin the display to the user
    # All other variable validation is done through type hints only
    if type(start_minute) != int:
        raise TypeError("The starting minute must be an integer")

    minute = start_minute

    def reset_clicked():
        """Controls the display and resetting of the timer during or after the timer has run its course."""
        global minute, second

        if (timer is None) or (minute == start_minute):
            return

        if start_minute < 10:
            sm = f"0{start_minute}"
        else:
            sm = f"{start_minute}"

        canvas.itemconfig(timer_id, text=f"{sm}:00")

        if (minute == 0) and (second == 0):
            canvas.itemconfig(timer_id, text=f"00:00")
            check_label.config(text="")
        else:
            reset_label.config(text="Start Again")
        minute = start_minute
        second = 0
        window.after_cancel(timer)
        # minute = start_minute

    def start_clicked():
        """Controls the starting of the timer at program run time or after the reset button has been pressed."""

        global minute, second

        # Guarantees that the start button can only be pressed at run time or after the reset button
        if minute != start_minute:
            return

        reset_label.config(text="")

        timer_start(minute, second)

    def timer_start(m, s):
        """Controls the display and running of the timer working with global variables."""
        global minute, second
        minute = m
        second = s
        if second < 10:
            sec = f"0{second}"
        else:
            sec = str(second)

        if minute < 10:
            minute_str = f"0{minute}"
        else:
            minute_str = str(minute)

        canvas.itemconfig(timer_id, text="{}:{}".format(minute_str, sec))

        if (minute == 0) and (second == 0):
            check_label.config(text="\u2713")  # Displays a check mark indicating the completing of the timer
            return

        if second == 0:
            second = 60
            minute -= 1
        global timer
        timer = window.after(1000, timer_start, minute, second - 1)

    # USER INTERFACE starts here- WINDOW GRID from TOP to BOTTOM, LEFT to RIGHT
    window = Tk()
    window.title("Pomodoro Timer")
    window.config(padx=100, pady=25, bg=YELLOW)

    # Timer Label
    timer_label = Label(text=timer_type.capitalize(), font=(FONT_NAME, 55, "bold"), bg=YELLOW, fg=GREEN,
                        padx=20, pady=25)
    timer_label.grid(column=1, row=0)

    # Tomato Image on Canvas
    im = PIL.Image.open("tomato.png")
    tomato_img = PIL.ImageTk.PhotoImage(im)

    canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
    canvas.create_image(100, 112, image=tomato_img)
    timer_id = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, "bold"))
    canvas.grid(column=1, row=1)

    # Start and Reset Buttons
    start_button = Button(text="Start", command=start_clicked)
    start_button.config(highlightbackground=YELLOW)
    start_button.grid(column=0, row=2)

    stop_button = Button(text="Reset", command=reset_clicked)
    stop_button.config(highlightbackground=YELLOW)
    stop_button.grid(column=2, row=2)

    # Reset Label
    reset_label = Label(bg=YELLOW, font=(FONT_NAME, 25, "bold"), fg=GREEN)
    reset_label.grid(column=1, row=3)

    # Finished Label
    check_label = Label(bg=YELLOW, font=(FONT_NAME, 70, "bold"), fg=GREEN)
    check_label.grid(column=1, row=4)

    window.mainloop()


def multi_pomodoro(number_of_reps: int = 4, work_time: int = 25, break_time: int = 5, final_break_time: int = 20):
    """A function that calls the pomodoro timer and creates a full cycle of pomodoro timers for work and break."""
    if number_of_reps != 0:
        for i in range(number_of_reps):
            global second
            pomodoro(work_time, 'work')
            second = 0
            if i == number_of_reps - 1:
                pomodoro(final_break_time, 'break')
            else:
                pomodoro(break_time, 'break')
            second = 0
    else:
        pomodoro()


if __name__ == '__main__':
    pass
