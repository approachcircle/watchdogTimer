while True:
    f = open("!watchdogs/1.$WDSTATE$", "w")
    f.write("0")  # infinitely writes a zero to the watchdog state file, throwing it off.
    f.close()
