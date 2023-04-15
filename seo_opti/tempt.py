import tkinter as tk
from tkinter import simpledialog
def create_custom_dialog(parent, previous_text):
    """
    Creates a custom dialog window with a text area and "Done" and "Add more" buttons.
    Returns the text area widget.
    """
    dialog = tk.Toplevel(parent)
    dialog.title("User Input")

    label = tk.Label(dialog, text="Please enter some text:")
    label.pack()

    text_area = tk.Text(dialog)
    text_area.pack()

    if previous_text:
        text_area.insert("1.0", previous_text + "\nnth try\n\n")

    done_button = tk.Button(dialog, text="Done", command=lambda: save_and_close_dialog(text_area, dialog, previous_text))
    done_button.pack(side="left")

    add_more_button = tk.Button(dialog, text="Add more", command=lambda: add_more_text(text_area))
    add_more_button.pack(side="right")

    return text_area

def add_more_text(text_area):
    """
    Adds the contents of the text area to the previous text and clears the text area.
    """
    new_text = text_area.get("1.0", "end-1c")
    previous_text = new_text.rstrip("\n")
    text_area.delete("1.0", "end")
    text_area.insert("1.0", previous_text + "\nnth try\n\n")

def save_and_close_dialog(text_area, dialog, previous_text):
    """
    Saves the contents of the text area to a file and closes the dialog window.
    """
    new_text = text_area.get("1.0", "end-1c")
    with open("input.txt", "a") as f:
        if previous_text:
            f.write(previous_text + "\n")
        f.write(new_text + "\n")
    dialog.destroy()
def get_user_text():
    """
    Prompts the user to enter some text and returns it as a list of lines.
    """
    # Create a Tkinter root window
    root = tk.Tk()
    root.withdraw()

    # Read any previous text from the file
    with open("input.txt", "r") as f:
        previous_text = f.read().rstrip("\n")

    # Create a custom dialog window
    text_area = create_custom_dialog(root, previous_text)

    # Wait for the dialog to be closed
    text_area.wait_window()

    # Read the saved text from the file and return it as a list of lines
    with open("input.txt", "r") as f:
        return f.readlines()
def main():
    get_user_text()
if __name__ == "__main__":
    main()