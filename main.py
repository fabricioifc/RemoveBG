from rembg import remove
from PIL import Image
from tqdm import tqdm
import os, argparse

class RemoveBackground:
    def __init__(self, input_folder, output_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.list_of_images = []

        os.makedirs(self.output_folder, exist_ok=True)
        assert os.path.exists(self.input_folder), "Input folder does not exist"
        assert os.path.exists(self.output_folder), "Output folder does not exist"

    def load_images(self):
        self.list_of_images = os.listdir(self.input_folder)
        print(f"Found {len(self.list_of_images)} images in the input folder")

    def remove_background(self):
        for image in tqdm(self.list_of_images):
            output_image_name = image.split(".")[0] + ".png"
            input_path = os.path.join(self.input_folder, image)
            output_path = os.path.join(self.output_folder, output_image_name)
            input_image = Image.open(input_path)
            output_image = remove(input_image)
            output_image.save(output_path, "PNG")

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--input_folder", type=str, help="Path to the input folder", default="input")
    args.add_argument("--output_folder", type=str, help="Path to the output folder", default="output")
    args = args.parse_args()
    remove_background = RemoveBackground(args.input_folder, args.output_folder)
    remove_background.load_images()
    remove_background.remove_background()
