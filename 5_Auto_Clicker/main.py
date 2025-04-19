import pyautogui
import time

def auto_click(inter, dur):
    end = time.time() + dur

    while time.time() < end:
        pyautogui.click()
        time.sleep(inter)

def main():
    print("Let's Begin..")
    auto_click(inter=5, dur=10000000000000)
    print("Aapna safar bas yahi tak tha...")

if __name__ == "__main__":
    main()