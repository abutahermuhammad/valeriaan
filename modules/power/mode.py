import subprocess
import sys
import platform


def logout():
    system_name = platform.system()

    if system_name == "Linux":
        subprocess.call(["logout"])
    elif system_name == "Windows":
        subprocess.call(["shutdown", "/l"])
    elif system_name == "Darwin":
        subprocess.call(
            ["osascript", "-e", "tell app \"System Events\" to log out"])
    else:
        print("Unsupported operating system")
        sys.exit(1)


def suspend():
    system_name = platform.system()

    if system_name == "Linux":
        subprocess.call(["systemctl", "suspend"])
    elif system_name == "Windows":
        subprocess.call(
            ["rundll32.exe", "powrprof.dll,SetSuspendState", "0", "1", "0"])
    elif system_name == "Darwin":
        subprocess.call(["pmset", "sleepnow"])
    else:
        print("Unsupported operating system")
        sys.exit(1)


def hibernate():
    system_name = platform.system()

    if system_name == "Linux":
        subprocess.call(["systemctl", "hibernate"])
    elif system_name == "Windows":
        subprocess.call(["shutdown", "/h"])
    elif system_name == "Darwin":
        print("Hibernation is not supported on macOS")
    else:
        print("Unsupported operating system")
        sys.exit(1)
