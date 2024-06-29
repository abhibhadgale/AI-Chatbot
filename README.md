# WhatsApp to ChatGPT Automated Message Bot
This project is an automated bot that copies the last message from a WhatsApp chat, sends it to ChatGPT, and replies with the response back on WhatsApp. It uses Python libraries pyautogui for automating mouse and keyboard actions, and pyperclip for clipboard operations.



Features:

Automatically selects and copies the last message from a WhatsApp chat.
Sends the copied message to ChatGPT.
Retrieves the response from ChatGPT.
Sends the ChatGPT response back to the WhatsApp chat.



Requirements:

Python 3.x
pyautogui
pyperclip



Installation:

Install Python 3.x from python.org.
Install the required libraries: pip install pyautogui pyperclip
Clone this repository: git clone https://github.com/your-username/whatsapp-chatgpt-bot.git
cd whatsapp-chatgpt-bot



Usage:

Open WhatsApp and ChatGPT in your browser and ensure their windows are visible on the screen.
Adjust the coordinates in the script to match your screen setup. The coordinates are specific to your screen resolution and window positions. You can find the coordinates using a tool like pyautogui.
Run the script: python bot.py



Code Explanation:

click_and_copy_text Function:
This function automates the process of selecting and copying the last message from WhatsApp.
def click_and_copy_text():
    pyautogui.click(654, 751)
    time.sleep(1)
    pyautogui.moveTo(538, 366)
    pyautogui.dragTo(814, 667, duration=1, button='left')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    clipboard_content = pyperclip.paste()
    pyautogui.click(920, 573)
    return clipboard_content
    
get_last_message Function:
This function processes the clipboard content to extract the sender and the message.
def get_last_message(clipboard_content):
    lines = clipboard_content.strip().split('\n')
    last_message = lines[-1] if lines else None
    if last_message:
        parts = last_message.split('] ', 1)
        if len(parts) > 1:
            sender_and_message = parts[1]
            sender, message = sender_and_message.split(': ', 1)
            return sender, message
    return None, None

send_message Function:
This function sends the copied message to ChatGPT and retrieves the response.
def send_message(sender, message):
    pyperclip.copy(message)
    copied_message = pyperclip.paste()
    pyautogui.click(143, 18)
    time.sleep(1)
    pyautogui.click(577, 605)
    time.sleep(1)
    pyautogui.typewrite(copied_message)
    pyautogui.hotkey('enter')
    time.sleep(5)
    pyautogui.moveTo(447, 296)
    pyautogui.dragTo(1172, 572, duration=1, button='left')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    clipboard_content = pyperclip.paste()
    pyautogui.click(323, 329)
    lines = clipboard_content.strip().split('\n')
    reply = lines[-1] if lines else None
    pyautogui.click(316, 16)
    pyautogui.click(900, 700)
    pyautogui.typewrite(reply)
    pyautogui.hotkey('enter')
    print(f"Sent message: {reply}")

Main Function:
The main function orchestrates the process by calling the above functions.
def main():
    clipboard_content = click_and_copy_text()
    print("Clipboard content:", clipboard_content)
    sender, last_message = get_last_message(clipboard_content)
    if sender:
        if sender != "Abhishek Bhadgale":
            print(f"Last message sender: {sender}")
            last_message_from_sender = last_message
            print("Last message from sender:", last_message_from_sender)
            send_message(sender, last_message_from_sender)
        else:
            print("The last message is from Abhishek Bhadgale (me), no user message.")
    else:
        print("No sender information found in the last message.")

if __name__ == "__main__":
    main()



Notes:

Ensure that the coordinates in the script match your screen resolution and window positions. You may need to adjust them accordingly.
This script assumes that WhatsApp and ChatGPT are opened and visible on the screen.



Disclaimer:
Use this script responsibly and ensure that you have permission to automate interactions with the applications in question.

License:
This project is licensed under the MIT License. See the LICENSE file for details.
