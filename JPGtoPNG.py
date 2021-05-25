import sys
import os
from PIL import Image

#grab 1st and 2nd agrument from command line. actualy these are input folder and output folder.

image_folder = sys.argv[1]
output_folder = sys.argv[2]

#print(image_folder, output_folder)

#check if the output_folder exist in the system

if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    
for filename in os.listdir(image_folder):
#    print(filename)
    op_filename = filename.split('.')[0]
 #   print(op_filename)
    img = Image.open(f'{image_folder}/{filename}')  #i have used / here because i did not given / after input folder name at argument
    
    img.save(f'{output_folder}/{op_filename}.png','png')