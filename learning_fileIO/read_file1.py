# File will auto close if done with the -with-
with open('insights.txt', 'r') as myFile:
    content = myFile.read()

print(content)