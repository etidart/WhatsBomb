import eel
import pyautogui

eel.init("web")


@eel.expose
def bomb(t, txt):
    times = 0
    while times < t:
        pyautogui.typewrite(txt)
        pyautogui.press("enter")
        times = times + 1


eel.start("main.html", size=(700, 740))
