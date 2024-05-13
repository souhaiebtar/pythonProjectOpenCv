import pyautogui

def move_mouse_to_text(text):
    screen_width, screen_height = pyautogui.size()
    search_area = (0, 0, screen_width, screen_height)
    position = pyautogui.locateOnScreen(text, region=search_area, grayscale=True)

    if position is not None:
        x, y, width, height = position
        target_x = x + width // 2
        target_y = y + height // 2
        pyautogui.moveTo(target_x, target_y)
    else:
        print("Text not found on the screen.")

# Example usage
text_to_search = "Hello, World!"
move_mouse_to_text(text_to_search)