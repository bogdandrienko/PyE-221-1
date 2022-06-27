import os

file_src = 'folder/file.txt'

with open(file_src, 'r') as file:
    text = file.readlines()
    print(text)
    clear_text = []
    for i in text:
        if len(i) > 1:
            clear_text.append(i)
    print(f"clear_text: {clear_text}")

    clear_text1 = [x for x in text if len(x) > 1]
    print(f"clear_text1: {clear_text1}")

current_path = 'folder/new_folder'
try:
    os.mkdir(current_path)
except:
    pass

for text in clear_text:
    file_name = f"file_{clear_text.index(text)+1}"
    with open(f"{current_path}/{file_name}", 'w') as file:
        text = file.write(text)

os.remove(file_src)
