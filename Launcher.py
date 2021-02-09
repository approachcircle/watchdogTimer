import os, time
os.system("if exist a.dat (echo) else (echo Note that the session lock file needs to be deleted after the program is closed, in a real watchdog timer, the process never properly ends.)")
os.system("if exist a.dat (echo) else (pause)")
os.system("echo > a.dat")
os.system("queryExist.bat") #since i wanna be fancy and use multi language files, im gonna just execute this in a seperate batch file
#instead of just doing it here inline
