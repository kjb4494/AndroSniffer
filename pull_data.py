import subprocess


def adb_connect():
    try:
        # Nox Test
        # subprocess.call("adb connect 127.0.0.1:62001")
        subprocess.call("adb --version")
        print()
    except:
        print("adb not found error")
        return
    subprocess.call("adb shell ls -l /data/")


def adb_pull():
    pass
