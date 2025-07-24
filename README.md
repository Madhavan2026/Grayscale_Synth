# Grayscale Synth: Xerox Effect Visualizer

Grayscale Synth is a simple Python-based tool that lets you convert images into a black-and-white (binary) "Xerox effect" using grayscale thresholding. The project provides both static and interactive visualizations for understanding how grayscale histograms relate to thresholding.

---

## 📸 Features

- Convert images to grayscale and apply binary thresholding
- Display side-by-side comparison of:
  - Original Image
  - Grayscale Histogram
  - Thresholded (Xeroxed) Output
- Real-time interaction (via slider) to dynamically adjust threshold

---

## 🛠️ Requirements

- Python 3.7+
- OpenCV
- Matplotlib
- (Optional for interactive version) `ipywidgets` and `jupyter`

Install dependencies:

```bash
pip install opencv-python matplotlib ipywidgets
```

---

## 📁 File Structure

```
Grayscale_Synth/
├── ocr.py              # Simple grayscale thresholding and display
├── ocr_with_hist.py           # Shows histogram + binary output
├── interactive_threshold_slider.py   # (Coming Soon) Interactive threshold with slider
└── README.md
```

---

## 🚀 Usage

### 1. Basic Xerox Conversion

```bash
python ocr.py
```

Edit `image_path` in the file to point to your desired image. You can also change the `threshold_value`.

### 2. Histogram + Thresholding Visualizer

```bash
python ocr_with_hist.py
```

This will show:
- Original image
- Grayscale histogram with a red threshold line
- Output image (black & white)

### 3. Interactive Threshold Slider (Coming Soon)

Will allow dynamic threshold tuning using a slider and see real-time changes to the output image.

---

## 📝 Example Output

- `xeroxed_output.png` – Output from basic script
- `xeroxed_output_with_hist.png` – Output from histogram script

---

## 💡 Applications

- Preprocessing for OCR or computer vision tasks
- Image stylization
- Understanding histogram-based thresholding

---

## 🙌 Contributions

Feel free to fork and enhance:
- Add adaptive thresholding
- Add GUI
- Export settings to file

---

## 📃 License

This project is open source and free to use under the MIT License.
