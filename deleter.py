## This script helps to only select x number of images and its corresponsing captions

import os
import random
import shutil

image_folder = "Images" ## fill in path with any dataset (8k flickr)
captions_file = "captions.txt" ## fill in with path with the original captions.txt
output_folder = "selected_images" ## new folder for images
output_captions_file = "selected_captions.txt" ## new txt for captions

# Step 1: Select x random image names
all_images = [filename for filename in os.listdir(image_folder) if filename.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
selected_image_names = random.sample(all_images, 4000)
os.makedirs(output_folder, exist_ok=True)
for image_name in selected_image_names:
    source_image_path = os.path.join(image_folder, image_name)
    destination_image_path = os.path.join(output_folder, image_name)
    shutil.copyfile(source_image_path, destination_image_path)

print("Images copied", output_folder)
selected_captions = {}
with open(captions_file, 'r') as f:
    for line in f:
        parts = line.strip().split(',')
        if len(parts) == 2:
            image_name, caption = parts
            if image_name in selected_image_names:
                selected_captions[image_name] = caption


with open(output_captions_file, 'w') as f:
    for image_name, caption in selected_captions.items():
        f.write(f"{image_name},{caption}\n")

print("Captions copied", output_captions_file)
