import os
import shutil

root = input("Enter the full path of directory you want to sort: \n")

# add more extension if needed
dic = {"doc": "Word File", "py": "Python File", "docx": "Word File", "exe": "EXE file", "zip": "Zip File",
       "txt": "Text File", "html": "HTML File", "png": "Images", "jpg": "Images", "mp4": "Videos",
       "pptx": "PPT file", "ppt": "PPT file", "cpp": "C++ File", "xlsx": "Excel File", "xlx": "Excel File",
       "mp3": "Audio File", "c": "C File",
       "pdf": "PDF File"}
flag = False
list_ = os.listdir(root)
for file_ in list_:
    name, ext = os.path.splitext(file_)
    ext = ext[1:]  # store Extension

    if ext == '':  # if it is a directory then skip
        continue
    else:
        if ext in dic.keys():
            if os.path.exists(root + '/Sorted/' + dic[ext]):  # if the extension name file already exists
                shutil.move(root + '/' + file_,
                            root + '/Sorted/' + dic[ext] + '/' + file_)  # then move the current file
            else:
                os.makedirs(root + '/Sorted/' + dic[ext])  # otherwise create the directory
                shutil.move(root + '/' + file_, root + '/Sorted/' + dic[ext] + '/' + file_)  # then move the file
        else:
            if not os.path.exists(root + '/Sorted/Extra File'):
                os.makedirs(root + '/Sorted/Extra File')  # otherwise create the directory named "Extra File"
                shutil.move(root + '/' + file_, root + '/Sorted/Extra File/' + file_)
                # flag = True
            else:
                if os.path.isfile(root + '/Sorted/Extra File/' + file_):
                    continue
                shutil.move(root + '/' + file_, root + '/Sorted/Extra File/' + file_)
                # flag = True
