import numpy as np
from PIL import Image


def img2char(image_file, h, char, flatness=0.45):
    img = Image.open(image_file)
    img_width, img_height = img.size
    w = int(h * img_width // img_height / flatness)
    img = img.resize((w, h), Image.Resampling.LANCZOS)
    pixels = np.array(img.convert('L'))
    N = len(char)
    step = 256 / N
    result = []

    for i in range(h):
        line = []
        for j in range(w):
            idx = int(pixels[i, j] / step)
            idx = min(idx, N - 1)
            line.append(char[idx])
        result.append(''.join(line))

    ascii_art = '\n'.join(result)
    with open('res.txt', 'w', encoding='utf-8') as f:
        f.write(ascii_art)

if __name__ == '__main__':
    input_img = 'anya.PNG'  # image name
    height = 200                # output chars length
    chars = "@%#*+=-:. "
    img2char(input_img, height, chars)
