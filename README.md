# Python_task7
## Image Resizer and Backup Script

This Python script resizes all image files in a specified folder (/storage/emulated/0/photo) to a maximum size of 500x500 pixels, while maintaining the aspect ratio. It also creates a backup of the original images in a subfolder named backup.


---

## 📁 Folder Structure

/storage/emulated/0/photo/
├── image1.jpg
├── image2.png
├── ...
└── backup/
    ├── image1.jpg (original)
    └── image2.png (original)


---

## 📜 Features

Resizes .jpg, .jpeg, .png, .webp images

Preserves original aspect ratio using thumbnail()

Backs up original images before resizing

Skips unsupported file formats and already backed-up files



---

## 🛠 Requirements

Python 3.x

Pillow library


Install Pillow
```
pip install Pillow
```

---

## ▶️ How to Run
```
python img_resize.py
```
Make sure your target images are placed in /storage/emulated/0/photo before running the script.


---

## 🖼️ Sample Output

```
Backed up: ph1.jpg
Original size: (5860, 3907)
Resized size: (500, 333)
------
Backed up: ph2.jpg
Original size: (6000, 4000)
Resized size: (500, 333)
------
Backed up: ph3.jpg
Original size: (5464, 3643)
Resized size: (500, 333)
------
Backed up: ph4.jpg
Original size: (6885, 4534)
Resized size: (500, 329)
------
Backed up: ph5.jpg
Original size: (4160, 3120)
Resized size: (500, 375)
------
```
