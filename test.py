with open("example.txt", "r") as file:
    content = file.read()
 

with open("example.txt", "w") as file:
    file.write("Apple\n")
    file.write("Banana\n")
    file.write("Elderberry\n")
    file.write("Fig\n")
    file.write("Grape\n")
    file.write("Honeydew\n")
    file.write("Kiwi\n")
    file.write("Lemon\n")
    file.write("Lime\n")
    file.write("Mango\n")
    file.write("Melon\n")
    file.write("Nectarine\n")
    file.write("Orange\n")

with open("example.txt", "a") as file:
    file.write("Orange\n")


