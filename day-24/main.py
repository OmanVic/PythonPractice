# with open('my_file.txt') as file:
#     contents = file.read()
#     print(contents)

with open("/Users/USER/Desktop/new_file.txt", mode="a") as file:
    file.write("\nI am a student of MIT")
with open("../../../../../Desktop/new_file.txt") as file:
    content = file.read()
    print(content)