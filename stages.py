# Stage 5/5: Save the results
class MarkDownEditor:
    def __init__(self):
        self.formats = ["plain", "bold", "italic", "header", "link", "inline-code", "new-line", "ordered-list",
                        "unordered-list"]
        self.text = ""

    def header(self):
        while True:
            level = int(input("Level: "))
            if 1 <= level <= 6:
                break
            print("The level should be within the range of 1 to 6")
        self.text += "#" * level + " " + input("Text: ") + "\n"

    def bold(self):
        self.text += "**" + input("Text: ") + "**"

    def italic(self):
        self.text += "*" + input("Text: ") + "*"

    def plain(self):
        self.text += input("Text: ")

    def inline_code(self):
        self.text += "`" + input("Text: ") + "`"

    def new_line(self):
        self.text += "\n"

    def link(self):
        self.text += f"[{input('Label: ')}]({input('URL: ')})"

    def list(self, mode):
        while True:
            no_rows = int(input("Number of rows: "))
            if no_rows > 0:
                break
            print("The number of rows should be greater than zero")
        rows = [input(f"Row #{i + 1}: ") for i in range(no_rows)]
        if mode == "ordered-list":
            for i in range(no_rows):
                self.text += f"{i + 1}. {rows[i]}\n"
        else:
            for i in range(no_rows):
                self.text += f"*. {rows[i]}\n"

    def start(self):
        while True:
            mode = input("Choose a formatter: ")
            if mode not in (self.formats + ["!help", "!done"]):
                print("Unknown formatting type or command")
            elif mode == "!help":
                print("""Available formatters: plain bold italic header link inline-code new-line ordered-list \
unordered-list
Special commands: !help !done""")
            elif mode == "!done":
                file = open("output.md", "w")
                file.write(self.text)
                file.close()
                break
            else:
                if mode in ["ordered-list", "unordered-list"]:
                    self.list(mode)
                else:
                    eval("self." + mode.replace("-", "_") + "()")
                print(self.text)


mark_down = MarkDownEditor()
mark_down.start()

