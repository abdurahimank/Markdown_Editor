# Stage 2/5: How do I use it?
formats = ["plain", "bold", "italic", "header", "link", "inline-code", "ordered-list", "unordered-list", "new-line"]
while True:
    mode = input("Choose a formatter: ")
    if mode not in (formats + ["!help", "!done"]):
        print("Unknown formatting type or command")
    elif mode == "!help":
        print("""Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line
Special commands: !help !done""")
    elif mode == "!done":
        break
