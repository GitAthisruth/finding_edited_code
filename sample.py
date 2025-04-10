import os
import difflib


originalFilePath = r"C:\Users\LENOVO\Desktop\prizmora\finding_edited_code\org.py"
backupFilePath = "backup_file.py"
original_Basename = os.path.basename(originalFilePath)
backup_Basename = os.path.basename(backupFilePath)
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
            else:
                print("no code change")
            max_len = max(len(original_content),len(backup_File_Content))
            for index in range(max_len):
                original_File_Line = original_content[index].strip() if index < len(original_content) else "<no line>"
                backup_File_Line = backup_File_Content[index].strip() if index < len(backup_File_Content) else "<no line>"
                if original_File_Line != backup_File_Line:
                    print(f"line :{index+1} of {original_Basename} is changed from {backup_File_Line} to {original_File_Line} in backupfile: {backup_Basename}")

    else:
        with open(backupFilePath, "w") as g:
            g.write(original_content)
        print(f"Backup file created: {backupFilePath}")
