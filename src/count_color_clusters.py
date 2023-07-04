import numpy as np
from skimage import measure

def count_color_clusters(image_array):
    # Normalise array to 0-1
    image_array = image_array / 255.0

    # Define target colors
    red_target = np.array([1, 0, 0])
    blue_target = np.array([0, 0, 1])
    magenta_target = np.array([0.90, 0.05, 0.59])  # adjusted for #e60e97
    lightblue_target = np.array([0.13, 0.68, 0.89])  # adjusted for #22aee2

    # Define color difference threshold
    threshold = 0.3  # increased threshold

    # Identify color pixels
    red_pixels = np.linalg.norm(image_array - red_target, axis=-1) < threshold
    blue_pixels = np.linalg.norm(image_array - blue_target, axis=-1) < threshold
    magenta_pixels = np.linalg.norm(image_array - magenta_target, axis=-1) < threshold
    lightblue_pixels = np.linalg.norm(image_array -lightblue_target, axis=-1) < threshold

    # Add magenta to red and lightblue to blue
    red_pixels = red_pixels + magenta_pixels
    blue_pixels = blue_pixels + lightblue_pixels

    # Count clusters
    red_clusters = measure.label(red_pixels, connectivity=2)
    blue_clusters = measure.label(blue_pixels, connectivity=2)

    # Number of clusters is the maximum label value
    num_red_clusters = red_clusters.max()
    num_blue_clusters = blue_clusters.max()

    return num_red_clusters, num_blue_clusters
