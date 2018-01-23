import os
import subprocess

folder_with_photo = "E:\Phyton\Materials\Photo_2_5";
folder_with_result_photo = "E:\Phyton\Materials\Result";
list_of_photo = os.listdir(folder_with_photo)
for photo in list_of_photo:
    way_to_photo = os.path.join(folder_with_photo, photo)
    file_extension = os.path.splitext(way_to_photo)
    if file_extension[1].lower() == '.jpg':
        way_to_result_photo = os.path.join(folder_with_photo, file_extension[0] + "Resize" + file_extension[1])
        process = subprocess.run("convert {0} {1}".format(way_to_photo, way_to_result_photo))