import cv2
import os
import argparse


def extract_frames(video_path: str, output_folder: str) -> None:
    """Extract frames from an MP4 video and save them as images.

    Args:
        video_path (str): Path to the input video file.
        output_folder (str): Path to the folder to save the extracted frames.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError(f"Error opening video file: {video_path}")

    frame_idx = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_filename = os.path.join(output_folder, f"image_{frame_idx:05d}.jpg")

        cv2.imwrite(frame_filename, frame)
        frame_idx += 1

    cap.release()
    print(f"Extracted {frame_idx} frames from the video.")


def main(video_path: str, output_folder: str) -> None:
    """Main function to extract frames from video and save them as images.

    Args:
        video_path (str): Path to the input video file.
        output_folder (str): Path to the folder to save the extracted frames.
    """
    extract_frames(video_path, output_folder)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract frames from a video and save them as images.")
    parser.add_argument("video_path", type=str, help="Path to the input video file.")
    parser.add_argument("output_folder", type=str, help="Path to the folder to save the extracted frames.")
    args = parser.parse_args()

    main(args.video_path, args.output_folder)
