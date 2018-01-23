import os
import subprocess

folder_with_photo = "E:\Phyton\Материалы\Photo_2_5";
folder_with_result_photo = "E:\Phyton\Материалы\Result";
list_of_photo = os.listdir(folder_with_photo)
for photo in list_of_photo:
    way_to_photo = os.path.join(folder_with_photo, photo)
    file_extension = os.path.splitext(way_to_photo)
    if file_extension[1] == '.jpg':
        process = subprocess.run("convert {} -resize 200 {}".format(way_to_photo, os.path.join(folder_with_result_photo, file_extension[0] +
                                                                                               "Resize" + file_extension[1])))