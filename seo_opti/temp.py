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

    done_button = tk.Button(dialog, text="Done", command=lambda: dialog.destroy())
    done_button.pack(side="left")

    add_more_button = tk.Button(dialog, text="Add more", command=lambda: save_and_add_text(text_area))
    add_more_button.pack(side="right")

    return text_area

def save_and_add_text(text_area):
    """
    Saves the text from the text area to a file, clears the text area, and adds the saved text and "nth try"
    to the text area.
    """
    new_text = text_area.get("1.0", "end-1c")
    with open("input.txt", "a") as f:
        f.write(new_text + "\n")
    text_area.delete("1.0", "end")
    previous_text = new_text.rstrip("\n")
    text_area.insert("1.0", previous_text + "\nnth try\n\n")

def get_suffix(n):
    """
    Returns the appropriate suffix for a given number.
    """
    SUFFIXES = {1: "st", 2: "nd", 3: "rd"}
    n= int(str(n)[-1])
    if n in SUFFIXES:
        return SUFFIXES[n]
    else:
        return "th"

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

def process_text(text, add_more=False):
    """
    Takes a list of lines of text and processes it to add HTML tags as necessary.
    Returns the processed text as a string.
    """
    if add_more:
        # Get the previous text from the file
        with open("input.txt", "r") as f:
            previous_text = f.read().rstrip("\n")
        # Add the "nth try" text between the previous and the new text
        output_text = nt_term([previous_text, text[0]])
        for line in text[1:]:
            line = line.strip()
            if line:
                # check for image extensions and add them to img tags
                line = process_image_extensions(line)
                # check for video/audio extensions and add them to video or audio tags
                line = process_video_audio_extensions(line)
                # check for external links and add them to bold tags
                line = process_external_links(line)
                # add br tags between lines
                output_text += f"<p>{line}</p>\n<br>\n"
    else:
        # Process the input text as before
        output_text = f"<h1>{text[0].strip()}</h1>\n"
        for line in text[1:]:
            line = line.strip()
            if line:
                # check for image extensions and add them to img tags
                line = process_image_extensions(line)
                # check for video/audio extensions and add them to video or audio tags
                line = process_video_audio_extensions(line)
                # check for external links and add them to bold tags
                line = process_external_links(line)
                # add br tags between lines
                output_text += f"<p>{line}</p>\n<br>\n"
    return output_text

def nt_term(text):
    """
    Processes the input text and returns the output text with "nth try" added.
    """
    if not text: # Check if the list is empty
        return "<p>No input text provided.</p>"

    output_text = f"<h1>{text[0].strip()}</h1>\n"
    for i, line in enumerate(text[1:], start=1):
        suffix = get_suffix(i)
        output_text += f"<p>{line.strip()} ({i}{suffix} try)</p>\n<br>\n"
    return output_text


def process_image_extensions(line):
    """
    Takes a string and checks if it contains an image extension.
    If so, adds the extension to an img tag and returns the updated string.
    Otherwise, returns the original string.
    """
    image_extensions = [".jpg", ".jpeg", ".png", ".gif"]
    for extension in image_extensions:
        if extension in line:
            line = f'<img src="{line}" alt="image">'
            break
    return line

def process_video_audio_extensions(line):
    """
    Takes a string and checks if it contains a video or audio extension.
    If so, adds the extension to a video or audio tag and returns the updated string.
    Otherwise, returns the original string.
    """
    video_audio_extensions = [".mp4", ".avi", ".mov", ".mp3", ".wav", ".ogg"]
    for extension in video_audio_extensions:
        if extension in line:
            if extension in [".mp4", ".avi", ".mov"]:
                line = f'<video src="{line}" controls></video>'
            else:
                line = f'<audio src="{line}" controls></audio>'
            break
    return line

def process_external_links(line):
    """
    Takes a string and checks if it contains an external link.
    If so, adds the link to a bold tag and returns the updated string.
    Otherwise, returns the original string.
    """
    if "http" in line:
        start_index = line.index("http")
        url = line[start_index:].split()[0]
        title = url.split("//")[-1].split("/")[0]
        line = line[:start_index] + f'<b><a href="{url}">{title}</a></b>' + line[start_index+len(url):]
    return line

def write_output_text(output_text):
    """
    Writes the output text to the input file.
    """
    with open("input.txt", "w") as f:
        f.write(output_text)


def main():
    """
    Runs the main program.
    """
    text = get_user_text()
    output_text = process_text(text)
    write_output_text(output_text)


if __name__ == '__main__':
    main()
