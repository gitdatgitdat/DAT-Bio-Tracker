import Functions_for_user_data as fud

from tkcalendar import Calendar #, DateEntry

try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk

# TODO - DT -> Pandas, QT -> TK


#new_data = fud.query_user_data()
#fud.write_user_data(new_data, user_data)

# this function is from the tkcalendar tutorial: https://github.com/j4321/tkcalendar#howtos
def show_example_calendar():
    top = tk.Toplevel(root)

    cal = Calendar(top, selectmode='none')
    date = cal.datetime.today() + cal.timedelta(days=2)
    cal.calevent_create(date, 'Hello World', "message")
    cal.calevent_create(date, 'Reminder 2', 'reminder')
    cal.calevent_create(date + cal.timedelta(days=-2), 'Reminder 1', 'reminder')
    cal.calevent_create(date + cal.timedelta(days=3), 'Message', 'message')

    cal.tag_config('reminder', background='red', foreground='yellow')

    cal.pack(fill="both", expand=True)
    ttk.Label(top, text="Hover over the events.").pack()


root = tk.Tk()
root.title("DAT Biotracker")
mainframe = ttk.Frame(root, padding = "10 10 10 10")
mainframe.grid(column = 0, row = 0, sticky=(tk.N, tk.W, tk.E, tk.S))
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

ttk.Label(mainframe, text = "Welcome").grid(column = 2, row = 1, sticky = tk.N)

ttk.Button(mainframe, text = "Input", command = fud.query_user_data).grid(column = 1, row = 3, sticky = tk.S)
ttk.Button(mainframe, text = "Output", command = fud.plot_by_time).grid(column = 2, row = 3, sticky = tk.S)
ttk.Button(mainframe, text='Example calendar with events', command = show_example_calendar).grid(column = 3, row = 3, sticky = tk.S)

root.mainloop()
