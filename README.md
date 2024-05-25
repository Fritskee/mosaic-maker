
# Image Mosaic Creator 🖼️

Welcome to the **Image Mosaic Creator**! This Python script allows you to create an image mosaic from a folder of images. You can specify the number of images you want in the mosaic and the script will handle the rest.
I also included code that allows you to extract all the frames from a video and save them as images in a folder. This way, you can create a mosaic from a video as well.

## Features ✨

- Loads images from a specified folder.
- Creates an image mosaic with a specified number of images.
- Supports `.jpg`, `.jpeg`, and `.png` file formats.
- Ensures images are loaded in the correct order based on numerical values in filenames.
- Saves and displays the resulting mosaic.

## Installation 🛠️

To use this script, you'll need to have Python installed. Additionally, you need to install the following Python libraries:

```bash
pip install numpy opencv-python matplotlib
```

## Usage 🚀

You can run the script from the command line. Below are the instructions:

```bash
python mosaic_creator.py /path/to/image/folder --num_images 16 --output mosaic.jpg
```

### Arguments

- `folder` (str): Path to the folder containing images.
- `--num_images` (int, optional): Number of images to include in the mosaic (default is 16).
- `--output` (str, optional): Output path for the mosaic image (default is `mosaic.jpg`).

## Example 🎨

```bash
python mosaic_creator.py ./images --num_images 16 --output output_mosaic.jpg
```

This command will create a mosaic from images in the `./images` folder, using 16 images, and save the output as `output_mosaic.jpg`.

## Disclaimer ⚠️

The script assumes that the images in the folder are named with numerical values following an underscore (`_`). For example, `image_00001.jpg`, `image_00002.png`, etc. Please ensure your filenames follow this convention to load them in the correct order.


# Video to Frames Extractor 🎥

This script allows you to extract frames from an MP4 video file and save them as images in a specified folder. The frames are saved with filenames in the format `image_00001.jpg`, `image_00002.jpg`, etc.

## Usage 🚀

You can run the script from the command line. Below are the instructions:

```bash
python extract_frames.py /path/to/video.mp4 /path/to/output/folder
```

### Arguments

- `video_path` (str): Path to the input video file.
- `output_folder` (str): Path to the folder to save the extracted frames.

### Example 🎨

```bash
python extract_frames.py sample_video.mp4 ./output_frames
```

This command will extract all frames from `sample_video.mp4` and save them in the `./output_frames` folder with filenames `image_00001.jpg`, `image_00002.jpg`, etc.

## Contact 📧

For any questions you can start an issue, or feel free to reach out to me via [X.com](https://x.com/freddygump1).

