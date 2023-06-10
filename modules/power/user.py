import subprocess
import os
import platform


def logout():
    """Logout from the current session"""
    os_name = platform.system().lower()

    if os_name == "linux":
        desktop_env = get_desktop_environment()
        if desktop_env == "i3":
            subprocess.call(["i3-msg", "exit"])
        elif desktop_env == "gnome":
            subprocess.call(["gnome-session-quit", "--logout"])
        elif desktop_env == "kde":
            subprocess.call(["qdbus", "org.kde.ksmserver",
                            "/KSMServer", "logout", "0", "1", "1"])
        elif desktop_env == "xfce":
            subprocess.call(["xfce4-session-logout", "--logout"])

    elif os_name == "windows":
        subprocess.call(["shutdown", "/l"])

    elif os_name == "darwin":
        subprocess.call(
            ["osascript", "-e", 'tell app "System Events" to log out'])

    # Add support for other operating systems here


def lock():
    """Lock the screen"""
    os_name = platform.system().lower()

    if os_name == "linux":
        desktop_env = get_desktop_environment()
        if desktop_env == "i3":
            subprocess.call(["i3lock"])
        elif desktop_env == "gnome":
            subprocess.call(["gnome-screensaver-command", "-l"])
        elif desktop_env == "kde":
            subprocess.call(
                ["qdbus", "org.freedesktop.ScreenSaver", "/ScreenSaver", "Lock"])
        elif desktop_env == "xfce":
            subprocess.call(["xflock4"])

    elif os_name == "windows":
        subprocess.call(["rundll32.exe", "user32.dll,LockWorkStation"])

    elif os_name == "darwin":
        subprocess.call(
            ["/System/Library/CoreServices/Menu Extras/User.menu/Contents/Resources/CGSession", "-suspend"])

    # Add support for other operating systems here


def switch_user():
    """Switch user"""
    os_name = platform.system().lower()

    if os_name == "linux":
        desktop_env = get_desktop_environment()
        if desktop_env == "i3" or desktop_env == "gnome" or desktop_env == "xfce":
            subprocess.call(["dm-tool", "switch-to-greeter"])

    # Add support for other operating systems here


def switch_vt():
    """Switch virtual terminal"""
    os_name = platform.system().lower()

    if os_name == "linux":
        desktop_env = get_desktop_environment()
        if desktop_env == "i3" or desktop_env == "gnome" or desktop_env == "xfce":
            subprocess.call(["dm-tool", "switch-to-greeter"])

    # Add support for other operating systems here


def get_desktop_environment():
    """Get the current desktop environment"""
    try:
        desktop_session = os.environ.get("DESKTOP_SESSION")
        if desktop_session:
            return desktop_session.split("/")[-1]
    except Exception:
        pass

    try:
        current_desktop = os.environ.get("XDG_CURRENT_DESKTOP")
        if current_desktop:
            return current_desktop
    except Exception:
        pass

    return "unknown"
