import os 
# from pathlib import Path

originalFilePath = r"C:\Users\LENOVO\Desktop\prizmora\finding_edited_code\org.py"
if os.path.exists(originalFilePath):
    with open(originalFilePath,"r") as f:
        content = f.read()
    with open("org_file.py","w") as g:
            g.write(content)
else:
    print("file path not found")