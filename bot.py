import pyautogui
import time
import pyperclip

def click_and_copy_text():
    # Click on the WhatsApp window at the specified coordinates (adjust as needed)
    pyautogui.click(654, 751)
    time.sleep(1)  # Wait for WhatsApp to come into focus

    # Drag to select text from the specified start to end coordinates (adjust as needed)
    pyautogui.moveTo(538, 366)  # Starting point of the selection
    pyautogui.dragTo(814, 667, duration=1, button='left')  # End point of the selection
    time.sleep(1)  # Ensure the drag action is complete

    # Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)  # Wait for the clipboard action to complete

    # Get the clipboard content
    clipboard_content = pyperclip.paste()

    #click for unselect text
    pyautogui.click(920, 573)
    return clipboard_content

def get_last_message(clipboard_content):
    # Split the clipboard content into lines
    lines = clipboard_content.strip().split('\n')
    
     # Get the last line
    last_message = lines[-1] if lines else None
    
    if last_message:
        # Strip the timestamp and brackets
        parts = last_message.split('] ', 1)  # Split at the first occurrence of '] '
        
        if len(parts) > 1:
            # Get the sender and message part
            sender_and_message = parts[1]
            
            # Split the sender and the message
            sender, message = sender_and_message.split(': ', 1)
            
            return sender, message
        return None, None

def send_message(sender, message):

    # Copy the message text to the clipboard
    pyperclip.copy(message)
    copied_message = pyperclip.paste()

   

    # Click on the chatgpt window at the specified coordinates
    pyautogui.click(143, 18)
    time.sleep(1)  # Wait for chatgpt to come into focus
    
    # Click on the message box of chatgpt and send message
    pyautogui.click(577, 605)
    time.sleep(1)  # Wait for chatgpt to come into focus'
    pyautogui.typewrite(copied_message)
    pyautogui.hotkey('enter')
    time.sleep(5)

    # Drag to select text from the specified start to end coordinates (adjust as needed)
    pyautogui.moveTo(447,296)  # Starting point of the selection
    pyautogui.dragTo(1172, 572, duration=1, button='left')  # End point of the selection
    time.sleep(1)  # Ensure the drag action is complete

    # Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)  # Wait for the clipboard action to complete

    # Get the clipboard content
    clipboard_content = pyperclip.paste()

    #click for unselect text
    pyautogui.click(323, 329)

    # Split the clipboard content into lines
    lines = clipboard_content.strip().split('\n')
    # Get the last line
    reply = lines[-1] if lines else None


    pyautogui.click(316, 16)
    pyautogui.click(900, 700)
    pyautogui.typewrite(reply)
    pyautogui.hotkey('enter')
    print(f"Sent message: {reply}")


def main():
    clipboard_content = click_and_copy_text()
    
    # Print the clipboard content to verifyNice

    print("Clipboard content:", clipboard_content)
    
    # Check the last message sender
    sender, last_message = get_last_message(clipboard_content)
    
    if sender:
        if sender != "Abhishek Bhadgale":
            print(f"Last message sender: {sender}")
            # Store the last message in a variable
            last_message_from_sender = last_message
            print("Last message from sender:", last_message_from_sender)
            send_message(sender, last_message_from_sender)
        else:
            print("The last message is from Abhishek Bhadgale (me), no user message.")
    else:
        print("No sender information found in the last message.")

if __name__ == "__main__":
    main()
