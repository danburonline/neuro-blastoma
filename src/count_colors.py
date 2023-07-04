import numpy as np


def count_colors(image_array):
    # Normalise array to 0-1
    image_array = image_array / 255.0

    # Define target colors
    red_target = np.array([1, 0, 0])
    blue_target = np.array([0, 0, 1])
    magenta_target = np.array([0.90, 0.05, 0.59])  # adjusted for #e60e97
    lightblue_target = np.array([0.13, 0.68, 0.89])  # adjusted for #22aee2

    # Define color difference threshold
    threshold = 0.3  # increased threshold

    # Count colors
    red_pixels = np.linalg.norm(image_array - red_target, axis=-1) < threshold
    blue_pixels = np.linalg.norm(image_array - blue_target, axis=-1) < threshold
    magenta_pixels = np.linalg.norm(image_array - magenta_target, axis=-1) < threshold
    lightblue_pixels = np.linalg.norm(image_array - lightblue_target, axis=-1) < threshold

    # Add magenta to red and lightblue to blue
    red_pixels = red_pixels.sum() + magenta_pixels.sum()
    blue_pixels = blue_pixels.sum() + lightblue_pixels.sum()

    return red_pixels, blue_pixels
