# Project: Markdown Editor
# Stage 3/5: Text formatting
class MarkdownEditor:
    def __init__(self):
        self.text = ""

    def header(self):
        while True:
            level = int(input("Level: "))
            if 1 <= level <= 6:
                break
            print("The level should be within the range of 1 to 6")
        text = input("Text: ")
        if self.text:
            self.text += (("\n" + "#" * level) + " " + text + "\n")
        else:
            self.text += (("#" * level) + " " + text + "\n")

    def bold(self):
        text = input("Text: ")
        self.text += ("**" + text + "**")

    def italic(self):
        text = input("Text: ")
        self.text += ("*" + text + "*")

    def plain(self):
        text = input("Text: ")
        self.text += text

    def inline_code(self):
        text = input("Text: ")
        self.text += ("`" + text + "`")

    def new_line(self):
        self.text += "\n"

    def link(self):
        label = input("Label: ")
        url = input("URL: ")
        self.text += f"[{label}]({url})"

    def start(self):
        while True:
            option = input("Choose a formatter: ")
            if option == "!help":
                print("""Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line
Special commands: !help !done""")
            elif option == "!done":
                break
            elif option not in ["plain", "bold", "italic", "header", "link", "inline-code",
                                "ordered-list", "unordered-list", "new-line"]:
                print("Unknown formatting type or command")
            else:
                eval("self." + option.replace("-", "_") + "()")
                print(self.text)


editor = MarkdownEditor()
editor.start()
