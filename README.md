# OS Compatibility
At the time of writing this, the program is only designed to run on windows, because of the fact that that it executes commands using the windows shell and syntax, a version for linux could possibly be made in the future however.

# Which file do i run?
You need to run <b>"Launcher.py"</b> to create a session lock check to avoid conflicts of multiple instances. The session lock file does not interfere with the throwOffWD file at all.

# What about the directory and what are they used for?
The empty directory in this repository is still important, an exception will be thrown if it is not cloned alongside the other files. It is used to store the watchdog's state, and is used to log the watchdog failures.

# So what is this program exactly?
This is a rough python representation of what a watchdog timer does/is. A wikipedia article on a watchdog timer can be found <a href="https://en.wikipedia.org/wiki/Watchdog_timer">here</a>

# Okay, but how can i tell that this won't harm my PC?
The basic function of this program is to write a '0' and a '1' to the file at <b>!watchdogs/1.$WDSTATE$</b> depending on the time. Since this is a github repository, and this is python, you can always just read the code to help on your judgement on whether or not to run the program :)

# What's the log.bin file used for then?
This is used when the watchdog timer fails a check, it will log the time and date in which the failure happened, much like what Windows would do it the case of a Bug Check (BSOD)

# And what about throwOffWD.py?
This file can be used to throw off the watchdog timer, causing it to throw the violation exception. It's purpose was to test the watchdog violation's mechanism, but you can just run it if you're bored of the timer working correctly and you want to see something interesting happen.
