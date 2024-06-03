import argparse
import os
import re
from typing import List

import cv2
import matplotlib.pyplot as plt
import numpy as np


def load_images_from_folder(folder: str) -> List[np.ndarray]:
    """Load all images from a specified folder in the correct order.

    Args:
        folder (str): Path to the folder containing images.

    Returns:
        List[np.ndarray]: List of images loaded as numpy arrays.
    """
    images = []
    image_files = [
        f
        for f in os.listdir(folder)
        if re.match(r".*\.(jpg|jpeg|png)$", f, re.IGNORECASE)
    ]
    
    def extract_number(filename):
        match = re.search(r"-([0-9]+)\.", filename)
        return int(match.group(1)) if match else float('inf')

    image_files.sort(key=extract_number)

    for filename in image_files:
        img_path = os.path.join(folder, filename)
        img = cv2.imread(img_path)
        if img is not None:
            images.append(img)
    return images


def create_image_mosaic(images: List[np.ndarray], num_images: int) -> np.ndarray:
    """Create an image mosaic from a list of images.

    Args:
        images (List[np.ndarray]): List of images to include in the mosaic.
        num_images (int): Number of images to include in the mosaic.

    Returns:
        np.ndarray: The image mosaic as a numpy array.
    """
    # Calculate grid size
    grid_size = int(np.ceil(np.sqrt(num_images)))
    selected_images = images[:num_images]
    height, width, _ = selected_images[0].shape
    mosaic = np.zeros((grid_size * height, grid_size * width, 3), dtype=np.uint8)

    for idx, img in enumerate(selected_images):
        row = idx // grid_size
        col = idx % grid_size
        mosaic[row * height : (row + 1) * height, col * width : (col + 1) * width] = img

    return mosaic


def save_and_display_mosaic(mosaic: np.ndarray, output_path: str) -> None:
    """Save and display the created image mosaic.

    Args:
        mosaic (np.ndarray): The image mosaic to save and display.
        output_path (str): Path to save the mosaic image.
    """
    cv2.imwrite(output_path, mosaic)
    plt.imshow(cv2.cvtColor(mosaic, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    plt.show()


def sample_uniformly(images: List[np.ndarray], num_samples: int) -> List[np.ndarray]:
    """Sample a specified number of images uniformly from a list of images.

    Args:
        images (List[np.ndarray]): List of images to sample from.
        num_samples (int): Number of images to sample.

    Returns:
        List[np.ndarray]: List of uniformly sampled images.
    """
    total_images = len(images)
    if total_images <= num_samples:
        return images

    step = total_images / num_samples
    sampled_images = [images[int(i * step)] for i in range(num_samples)]
    return sampled_images


def main(folder: str, num_images: int, output_path: str) -> None:
    """Main function to create and save an image mosaic.

    Args:
        folder (str): Path to the folder containing images.
        num_images (int): Number of images to include in the mosaic.
        output_path (str): Path to save the mosaic image.
    """
    images = load_images_from_folder(folder)
    if len(images) < num_images:
        raise ValueError(
            "The folder contains fewer images than the specified number for the mosaic."
        )

    sampled_images = sample_uniformly(images, num_images)
    mosaic = create_image_mosaic(sampled_images, num_images)
    save_and_display_mosaic(mosaic, output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Create an image mosaic from a folder of images."
    )
    parser.add_argument("folder", type=str, help="Path to the folder containing images.")
    parser.add_argument(
        "--num_images",
        type=int,
        default=16,
        help="Number of images to include in the mosaic (default is 16).",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="mosaic.jpg",
        help="Output path for the mosaic image (default is 'mosaic.jpg').",
    )
    args = parser.parse_args()

    main(args.folder, args.num_images, args.output)
