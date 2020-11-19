def reader(character, filepath="insights.txt"):
    myFile = open(filepath)
    content = myFile.read()
    return content.count(character)

