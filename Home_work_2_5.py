import os
import subprocess

folder_with_photo = "Source";
folder_with_result_photo = "Result";
current_dir = os.path.dirname(os.path.abspath(__file__))

way_to_folder_with_photo = os.path.join(current_dir, folder_with_photo)
way_to_folder_with_result_photo = os.path.join(current_dir, folder_with_result_photo)

list_of_photo = os.listdir(way_to_folder_with_photo)
for photo in list_of_photo:
    way_to_photo = os.path.join(way_to_folder_with_photo, photo)
    file_extension = os.path.splitext(way_to_photo)
    if file_extension[1].lower() == '.jpg':
        way_to_result_photo = os.path.join(way_to_folder_with_result_photo, photo)
        process = os.popen("convert {} -resize 200 {}".format(way_to_photo, way_to_result_photo))