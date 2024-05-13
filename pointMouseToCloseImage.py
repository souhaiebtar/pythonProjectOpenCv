import cv2
import pyautogui

def find_button(image_path):
    # Load the target image
    target_image = cv2.imread(image_path)

    # Get the screen resolution
    screen_width, screen_height = pyautogui.size()

    # Get the dimensions of the target image
    target_width, target_height = target_image.shape[:-1]

    # Find the location of the target image on the screen
    result = cv2.matchTemplate(pyautogui.screenshot(), target_image, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    # Calculate the center coordinates of the target image
    target_center_x = max_loc[0] + target_width // 2
    target_center_y = max_loc[1] + target_height // 2

    # Calculate the corresponding mouse position
    mouse_x = target_center_x * screen_width // target_width
    mouse_y = target_center_y * screen_height // target_height

    # Move the mouse pointer to the button
    pyautogui.moveTo(mouse_x, mouse_y)

# Example usage
find_button('button.png')