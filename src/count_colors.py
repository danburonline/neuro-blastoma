def count_colors(image_array):
    # Normalise array to 0-1
    image_array = image_array / 255.0
    red_pixels = ((image_array[..., 0] > 0.5) & (image_array[..., 1] < 0.3)
                & (image_array[..., 2] < 0.3)).sum()
    blue_pixels = ((image_array[..., 0] < 0.3) & (image_array[..., 1] < 0.3)
                & (image_array[..., 2] > 0.5)).sum()
    return red_pixels, blue_pixels