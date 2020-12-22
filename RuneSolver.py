import pyautogui
import time
import win32api, win32con
from win32gui import *

reference_list = ["LEFT", "UP", "DOWN"]

def get_window_rect():
    # Get the coordinates of the active window
    rect = GetWindowRect(GetForegroundWindow())
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y
    return (x, y, w, h)

def final_prime(combo, cache):
    combo.extend(cache)
    combo.append("RIGHT")
    return combo

def find_rune_at_region(region):
    if pyautogui.locateOnScreen('left_rune_arrow.png', region=region, confidence=0.8) != None:
        return "LEFT"
    elif pyautogui.locateOnScreen('up_rune_arrow.png', region=region, confidence=0.8) != None:
        return "UP"
    elif pyautogui.locateOnScreen('down_rune_arrow.png', region=region, confidence=0.8) != None:
        return "DOWN"
    else:
        return False

def main():
    print("Giving 2 seconds, please click on the maplestory window.")
    time.sleep(2)
    rect = get_window_rect()
    first_rune_region = (rect[0] + 529, rect[1] + 253, 37, 37)
    second_rune_region = (rect[0] + 622, rect[1] + 253, 37, 37)
    # These regions are specific regions of the screen for the rune, DO NOT CHANGE

    cache = reference_list
    combo = []

    first_rune = find_rune_at_region(first_rune_region)
    cache.remove(first_rune)
    combo.append(first_rune)

    second_rune = find_rune_at_region(second_rune_region)
    cache.remove(second_rune)
    combo.append(second_rune)

    combo = final_prime(combo, cache)

    # combo is a list that stores all direction of the rune combination

    print("Rune Combination", combo)



if __name__ == '__main__':
    main()
