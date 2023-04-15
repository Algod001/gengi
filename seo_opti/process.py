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

