import keyboard
import pyperclip
import pyautogui
import time

def process_text():
    # Select all text
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.1)  # Small delay to ensure the action is performed
    
    # Copy selected text
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.1)  # Small delay to ensure the action is performed

    # Get the clipboard content
    clipboard_content = pyperclip.paste()

    # Split into words
    words = clipboard_content.split()
    
    # Process each word
    new_clipboard = ""
    for word in words:
        word_length = len(word)

        # Determine the number of characters to bold based on word length
        if word_length <= 3:
            bold_count = 1
        elif 4 <= word_length <= 6:
            bold_count = 2
        elif word_length == 7:
            bold_count = 3
        else:
            bold_count = 4

        # Add artificial fixation points to the specified number of characters
        modified_word = f"**{word[:bold_count]}**{word[bold_count:]}"
        
        # Concatenate modified word to the new clipboard content
        new_clipboard += modified_word + " "
    
    # Trim the new clipboard content to remove the trailing space
    new_clipboard = new_clipboard.strip()

    # Set modified content to clipboard
    pyperclip.copy(new_clipboard)

    # Paste the modified content
    pyautogui.hotkey('ctrl', 'v')
    
    # Press backspace to remove the trailing '+'
    pyautogui.press('backspace')

    # Press Enter
    pyautogui.press('enter')

# Set a hotkey (NumpadAdd) to trigger the process_text function
keyboard.add_hotkey('add', process_text)  # 'add' corresponds to the NumpadAdd key

# Keep the script running
keyboard.wait('esc')  # Stop the script with 'esc' key
