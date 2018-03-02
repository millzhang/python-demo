def word_count(filePath=""):
    try:
        with open(filePath, encoding="UTF-8") as fs:
            contents = fs.read()
    except FileNotFoundError:
        print(filePath + " is not exist!")
    else:
        result = str(len(contents.split()))
        print(filePath + " has " + result + " words!")
