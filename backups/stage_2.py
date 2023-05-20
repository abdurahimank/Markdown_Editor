# Project: Markdown Editor
# Stage 2/5: How do I use it?
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
