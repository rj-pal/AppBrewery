# Pomodoro Countdown Timer

The [Pomodoro Technique](https://en.wikipedia.org/wiki/Pomodoro_Technique) is a time management method to help you 
improve your concentration and productivity on a task. It is based on a timed 25-minute minute period of concentration where 
you focuss on the task-at-hand. After the timed work session ends, you take a short break and repeat the session again.
The method suggests using a special kitchen tomato timer and check list for every completed 25-minutes of concentration.

The *simple_timer script* will run a simple 25-minutes Pomodoro Timer.

The *series_timers script* will run a [full-cycle](https://todoist.com/productivity-methods/pomodoro-technique) series 
of Pomodoro Timers with **four 25-minute** 'Work' sessions, **three 5-minute** 'Break' sessions, and **one 20-minute** 'Final 
Break' session.

The *main script* allows the user to choose which type of timer they want and you can **control the reps and timing parameters**,
like final break time session. Details of those parameters are at the bottom of this document.

The *test_timer script* sets up a simple 1-minute timer and allows the user to test the start and reset buttons. Pressing
the start button multiple times will not affect the timer in progress. Pressing the reset button will reset the timer, 
and the user will have to press start again to run the timer. Once the timer is completed, a check mark will appear.
You still cannot start the timer again, until reset and start are pressed again in that order.

In the **pomodoro.py** file:
- The function **pomodoro()** defaults to a simple 25-minute timer. The time will initially be set at zero. After pressing the
start button, the timer will move to the initial start time 25:00 and begin to countdown. If reset is pressed at any time, the clock
will reset to the full time and not start again until the start button has been pressed again. Once the timer reaches zero, a 
check mark will appear. Pressing reset here will remove the check mark but keep the time at zero like in the original 
configuration, and won't countdown again until the start button is pressed.

  It has two parameters: *start_time* and *timer_type*. 
Start time allows the user to adjust the timer length. Timer type allows you to change the name of timer. The function also 
sets the configuration of the timer window and all the button and label features are controlled by this function.


- The function **multi_pomodoro()** is a series of work and break timers. Each timer is a new pomodoro() function timer.
After each timer finishes, the user will have to close the currently open timer with a final check, and a new timer will 
open. The cycle is four work sessions with three short break sessions one longer, final break session. Each timer will have a 
unique name of "Work' or "Break' to distinguish the timer type. The number of work sessions and all timer lenghts can be modified. 


  It has four parameters: *number_of_reps, work_time, break_time, final_break_time*. Number of reps will adjust the number of work 
sessions, *defaulted to 4 repetitions*. Work time adjusts the working session timer, *defaulted to 25 minutes*. Break time and 
Final break time parameters adjust the break session timers, *defaulted to 5 and 20 minutes*.
