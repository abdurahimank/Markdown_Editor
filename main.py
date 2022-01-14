def list_(x, y):
    while True:
        number_of_rows = int(input("Number of rows: "))
        if number_of_rows > 0:
            break
        else:
            print("The number of rows should be greater than zero")
            continue
    lis = [input(f"Row #{i + 1}: ") for i in range(number_of_rows)]
    if y == "ordered-list":
        for i in range(number_of_rows):
            x += f"{i + 1}. {lis[i]}\n"
    else:
        for i in range(number_of_rows):
            x += f"* {lis[i]}\n"
    return x


def new_line(x):
    # x += "<br>"  # For mark down language
    x += "\n"
    return x


def inline_code(x):
    text = input("Text: ")
    x += f"`{text}`"
    return x


def link(x):
    label = input("Label: ")
    url = input("URL: ")
    x += f"[{label}]({url})"
    return x


def italic(x):
    text = input("Text: ")
    x += f"*{text}*"
    return x


def bold(x):
    text = input("Text: ")
    x += f"**{text}**"
    return x


def plain(x):
    text = input("Text: ")
    x += f"{text}"
    return x


def header(x):
    while True:
        level = input("Level: ")
        if level.isdigit() and 1 <= int(level) <= 6:
            break
        else:
            print("The level should be within the range of 1 to 6")
    text = input("Text: ")
    x += f"{'#' * int(level)} {text}\n"
    return x


formatter_list = {"plain": plain, "bold": bold, "italic": italic, "header": header, "ordered-list": list_,
                  "unordered-list": list_, "link": link, "inline-code": inline_code, "line-break": new_line}
markdown = ""
while True:
    formatter = input("Choose a formatter: ")
    if formatter == "!help":
        print("""Available formatters: plain bold italic header link inline-code header new-line
Special commands: !help !done""")
        continue
    elif formatter == "!done":
        file_1 = open("output.md", "w")
        file_1.write(markdown)
        file_1.close()
        break
    elif formatter in formatter_list.keys():
        if formatter == "ordered-list" or formatter == "unordered-list":
            markdown = formatter_list[formatter](markdown, formatter)
        else:
            markdown = formatter_list[formatter](markdown)
        print(markdown)
    else:
        print("Unknown formatting type or command")
