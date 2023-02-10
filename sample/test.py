from curses import initscr, endwin
from signal import signal, SIGWINCH
from time import sleep

stdscr = initscr()

def redraw_stdscreen():
    rows, cols = stdscr.getmaxyx()
    stdscr.clear()
    stdscr.border()
    stdscr.hline(2, 1, '_', cols-2)
    stdscr.refresh()

def resize_handler(signum, frame):
    endwin()  # This could lead to crashes according to below comment
    stdscr.refresh()
    redraw_stdscreen()

signal(SIGWINCH, resize_handler)

initscr()

try:
    redraw_stdscreen()

    while 1:
        # print stuff with curses
        sleep(1)
except (KeyboardInterrupt, SystemExit):
    pass
except Exception as e:
    pass

endwin()
