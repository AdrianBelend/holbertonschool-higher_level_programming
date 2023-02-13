    #!/usr/bin/python3
"""defines a function that writes a string into a text file"""


def write_file(filename="", text=""):
    """function """
    with open(filename, "w", encoding="utf-8") as file:
        filetext = file.write(text)
        return filetext
