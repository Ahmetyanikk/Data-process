#CREATE MULTIPLE INSTANCES FROM A SOURCE FILE
#1. Instance-Source File, 2. The Part Wanted to be Changed, 3. The Part Wanted to be Changed New Version
#4. Special Name for your Copies, 5. Directory to be saved, Extension(like .py)
#Note: Chance special_file_name in for loop like "example_"+str(i)
def createFile(source_file_path, part_you_want_change, part_you_want_change_new, special_file_name, directry_to_save, extension):
    with open(source_file_path, "r") as file:
        content = file.read()
    file.close()
    
    content_new = content.replace(part_you_want_change, part_you_want_change_new)

    with open(directry_to_save + special_file_name + extension, "w") as file1:
        file1.write(content_new)
    file1.close()
