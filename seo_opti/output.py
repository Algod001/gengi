def write_output_text(output_text):
    """
    Writes the output text to the input file.
    """
    with open("input.txt", "w") as f:
        f.write(output_text)

