#!/usr/bin/env python3
import csv
import math
from PIL import Image

# Define the target colours and their labels.
# Each tuple is (RGB tuple, label)
TARGET_COLORS = [
    ((255, 255, 255), "white"),
    ((0, 0, 0), "black"),
    ((173, 216, 230), "blue")
]

# Alpha threshold to consider a pixel "transparent"
ALPHA_THRESHOLD = 128

def closest_color_label(r, g, b):
    """Return the label of the target colour that is closest to (r, g, b)."""
    best_label = None
    best_dist_sq = float('inf')
    for (tr, tg, tb), label in TARGET_COLORS:
        # Compute squared Euclidean distance (no need to take sqrt)
        dist_sq = (r - tr) ** 2 + (g - tg) ** 2 + (b - tb) ** 2
        if dist_sq < best_dist_sq:
            best_dist_sq = dist_sq
            best_label = label
    return best_label

def process_image(input_filename, output_filename):
    try:
        # Open image and ensure it has an alpha channel (RGBA)
        img = Image.open(input_filename).convert("RGBA")
    except Exception as e:
        print(f"Error opening {input_filename}: {e}")
        return

    width, height = img.size
    pixels = img.load()

    # Prepare the output data as a list of lists (rows)
    cell_data = []
    for y in range(height):
        row_data = []
        for x in range(width):
            r, g, b, a = pixels[x, y]
            if a < ALPHA_THRESHOLD:
                row_data.append("")
            else:
                # Map the pixel to the closest target colour label.
                label = closest_color_label(r, g, b)
                row_data.append(label)
        cell_data.append(row_data)

    # Write the cell data to a CSV file.
    try:
        with open(output_filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(cell_data)
        print(f"Output written to {output_filename}")
    except Exception as e:
        print(f"Error writing {output_filename}: {e}")

def main():
    # Process the two cloud images.
    images = [("single.png", "single.csv"), ("triple.png", "triple.csv")]
    for input_file, output_file in images:
        process_image(input_file, output_file)

if __name__ == "__main__":
    main()
