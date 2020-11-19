with open("test.txt", "a+") as file:
    content = file.write("Even more sample text")
    file.seek(0)
    content = file.read()

print(content)