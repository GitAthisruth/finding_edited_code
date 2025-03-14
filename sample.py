import os
import difflib

originalFilePath = r"C:\Users\LENOVO\Desktop\prizmora\finding_edited_code\org.py"
backupFilePath = "backup_file.py"
if os.path.exists(originalFilePath):
    with open(originalFilePath,"r") as f:
        original_content = f.readlines()
        # print(f"originalContent:{original_content}")
    if os.path.exists(backupFilePath):
        with open(backupFilePath,"r") as g:
            backup_File_Content = g.readlines()
            # print(f"backup_File_Content:{backup_File_Content}")
            if original_content != backup_File_Content:
                print(f"editing file is modified..")
                for index in range(len(original_content)):
                    if original_content[index]!=backup_File_Content[index]:
                        print(f"line :{index+1} of original_content is changed from {backup_File_Content[index]} to {original_content[index]}")

    else:
        with open(backupFilePath, "w") as g:
            g.write(original_content)
        print(f"Backup file created: {backupFilePath}")
