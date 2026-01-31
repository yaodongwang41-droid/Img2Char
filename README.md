# Image to ASCII Art Converter

A lightweight Python script that transforms images into stylized ASCII art using grayscale mapping.

## 🚀 Features
* **Grayscale Mapping**: Converts image pixels to a custom character set (`@%#*+=-:. `) based on brightness.
* **Aspect Ratio Correction**: Automatically compensates for the vertical stretch of text characters to maintain the original image proportions.
* **File Export**: Saves the final result directly to a `.txt` file for easy sharing.

## 🛠️ Prerequisites
You will need `Python 3.x` and the following libraries:
* **Pillow**: For image processing.
* **NumPy**: For efficient matrix operations.

```bash
pip install pillow numpy

```

## 📋 How to Use

* **Prepare Image**: Place your source image (e.g., anya.PNG) in the same directory as the script.

* **Configure**: Update the image_file variable in the script with your filename.

```bash
Run:python main.py
```
## ⚠️ Important: Viewing Instructions
To ensure the art displays correctly without distortion or horizontal stretching, please adjust your text editor (Notepad, VS Code, TextEdit, etc.) settings:

* **Use Monospaced Fonts**: You must use a fixed-width (monospaced) font such as Consolas, Courier New, or Lucida Console. Non-monospaced fonts will break the alignment.

* **Disable Word Wrap**: Ensure "Word Wrap" is turned OFF so the lines don't break prematurely.

* **Zoom Out**: ASCII art often requires a very small font size or a low zoom level to be viewed correctly on standard screens.

## ⚙️ Customization
You can easily tweak the output by modifying these variables:

* **height**: Adjusts the number of rows in the output (default is 200).

* **chars**: Change the character string to use different symbols. The order represents the gradient from dark to light.

* **0.45**: The scale factor used to balance character width vs. height (since characters are usually taller than they are wide).