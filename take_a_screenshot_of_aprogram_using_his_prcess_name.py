import pyautogui
import psutil

def take_screenshot_by_process_name(process_name, output_file):
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == process_name:
            pid = proc.pid
            pyautogui.screenshot(output_file, region=pyautogui.getWindowsWithTitle(process_name)[0].left, top, width, height)
            break

# Usage example
process_name = "notepad.exe"
output_file = "screenshot.png"
take_screenshot_by_process_name(process_name, output_file)


