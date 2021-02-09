import traceback
try:
    class SessionLockedException(Exception):
        pass
    raise SessionLockedException("Session has already been locked. Possibly by another instance?")
except SessionLockedException:
    traceback.print_exc()
    print()
    print("Press enter.")
    input()
