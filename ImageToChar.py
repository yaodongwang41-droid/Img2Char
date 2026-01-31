import numpy as np
from PIL import Image

if __name__ == '__main__':
    image_file = 'anya.PNG'  # input figure
    height = 200                # output chars length
    img = Image.open(image_file)
    img_width, img_height = img.size
    width = int(height * img_width // img_height / 0.45)
    img = img.resize((width, height),Image.Resampling.LANCZOS)
    pixels = np.array(img.convert('L'))
    chars = "@%#*+=-:. "
    N = len(chars)
    step = 256 / N

    result = []

    for i in range(height):
        line = []
        for j in range(width):
            idx = int(pixels[i, j] / step)
            idx = min(idx, N - 1)
            line.append(chars[idx])
        result.append(''.join(line))

    ascii_art = '\n'.join(result)
    with open('res.txt', 'w', encoding='utf-8') as f:
        f.write(ascii_art)
