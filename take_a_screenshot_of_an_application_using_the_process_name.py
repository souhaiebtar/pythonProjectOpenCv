import pygetwindow as gw
import pyautogui

# take a screenshot of an application using the process name 
def take_screenshot(process_name):
    try:
        # Get the window with the specified process name
        window = gw.getWindowsWithTitle(process_name)[0]

        # Activate the window
        window.activate()

        # Get the window's position and size
        x, y, width, height = window.left, window.top, window.width, window.height

        # Take a screenshot of the window
        screenshot = pyautogui.screenshot(region=(x, y, width, height))

        # Save the screenshot to a file
        screenshot.save('screenshot.png')

        print("Screenshot taken successfully!")
    except IndexError:
        print("No window found with the specified process name.")

# Specify the process name of the application you want to take a screenshot of
process_name = "example.exe"

# Call the function to take the screenshot
take_screenshot(process_name)
