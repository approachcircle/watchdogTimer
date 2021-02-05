import traceback, time, os, sys, winsound
os.system("echo > SESSION.LOCK")
z = 0
x = 1
try:
    t = 5
    wdid = 0
    def countdown(t):
        while t > z:
            print(t)
            t -= x
            time.sleep(1)

    while True:
        f = open("C:/Windows/!watchdogs/1.$WDSTATE$", "r")
        print("WATCHDOG KICKED")
        print(time.ctime())
        print()
        time.sleep(0.25)
        f = open("C:/Windows/!watchdogs/1.$WDSTATE$", "w")
        f.write("1")
        f.close()
        f = open("C:/Windows/!watchdogs/1.$WDSTATE$", "r")
        returned = f.read()
        if returned == "1":
            f = open("C:/Windows/!watchdogs/1.$WDSTATE$", "w")
            f.write("0")
            f.close()
            f = open("C:/Windows/!watchdogs/1.$WDSTATE$", "r")
            returned = f.read()
            if returned == "0":
                pass
            else:
                raise ZeroDivisionError
        else:
            raise ZeroDivisionError
    os.system("del SESSION.LOCK")

except FileNotFoundError:
    print("TRACEBACK BUGCHECK")
    print("A fatal error occured and the program needs immediate attention.")
    print("The watchdog state file which is required is missing. (at the path of C:/Windows/!watchdogs/)")
    winsound.Beep(500,950)
    input("Press enter to see the stacktrace information:")
    print()
    traceback.print_exc()
    input("END:")
    os.system("del SESSION.LOCK")
    sys.exit()

except ZeroDivisionError:
    print("TRACEBACK BUGCHECK")
    print("A fatal error occured and the program needs to restart in order to continue operation.")
    print()
    print("WATCHDOG_VIOLATION")
    print()
    winsound.Beep(500,950)
    time.sleep(0.25)
    winsound.Beep(500,950)
    time.sleep(0.25)
    winsound.Beep(500,950)
    print("DUMPING CRASH INFO. DO NOT TURN OFF YOUR COMPUTER...")
    f = open("C:/Windows/!watchdogs/log.bin", "w")
    f.write("WATCHDOG_VIOLATION AT " + time.ctime())
    f.close()
    time.sleep(2)
    os.system("cls")
    print("DONE")
    time.sleep(0.2)
    print("RESTART IN...")
    countdown(t)
    os.system("cls")
    os.system("python D:/Python/watchdogTimer.py")
    os.system("del SESSION.LOCK")
    sys.exit()

except Exception:
    print("TRACEBACK BUGCHECK")
    print("A fatal error occured and the program needs immediate attention.")
    print("the program cannot identify the problem.")
    winsound.Beep(500,950)
    time.sleep(0.25)
    winsound.Beep(500,950)
    input("Press enter to see the stacktrace information:")
    print()
    print("Fell back to General Exception SuperClass")
    print()
    traceback.print_exc()
    input("END:")
    os.system("del SESSION.LOCK")
    sys.exit()
