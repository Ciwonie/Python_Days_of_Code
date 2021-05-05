

# we no longer have to remember to close the file because of the "with' keyword
with open(file="new_file.txt", mode="w") as file:
    file.write("I created a new file\n")
