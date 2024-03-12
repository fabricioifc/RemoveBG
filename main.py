from rembg import remove, new_session
from PIL import Image
from tqdm import tqdm
import os, argparse

# MODEL_NAME = "silueta"

class RemoveBackground:
    def __init__(self, input_folder, output_folder, model_name):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.model_name = model_name
        self.list_of_images = []

        os.makedirs(self.output_folder, exist_ok=True)
        assert os.path.exists(self.input_folder), "Input folder does not exist"
        assert os.path.exists(self.output_folder), "Output folder does not exist"

        # print information
        print(f"Model name: {self.model_name}")


    def load_images(self):
        self.list_of_images = os.listdir(self.input_folder)
        print(f"Found {len(self.list_of_images)} images in the input folder")

    def remove_background(self):
        print("Removing background...")
        session = new_session(self.model_name)
        print(f"Session created for {self.model_name}")
        print(f"Session ID: {session}")
        for image in tqdm(self.list_of_images):
            output_image_name = image.split(".")[0] + ".png"
            input_path = os.path.join(self.input_folder, image)
            output_path = os.path.join(self.output_folder, output_image_name)
            input_image = Image.open(input_path)
            output_image = remove(input_image, session=session)
            output_image.save(output_path, "PNG")

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--input_folder", type=str, help="Path to the input folder", default="input")
    args.add_argument("--output_folder", type=str, help="Path to the output folder", default="output")
    args.add_argument("--model_name", type=str, help="Name of the model to use", default="silueta")
    
    args = args.parse_args()
    remove_background = RemoveBackground(args.input_folder, args.output_folder, args.model_name)
    remove_background.load_images()
    remove_background.remove_background()
