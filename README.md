# Meme Generator (Python + GUI)

## Overview
This is a desktop-based Meme Generator built using Python.  
It allows users to generate memes using random image templates and logically paired captions, with an optional graphical interface.

The project focuses on **clean code structure**, **logic-driven randomness**, and **separation of concerns**, rather than quick hacks.

---

## Features
- Random meme template selection from a folder
- Caption generator with **logical pairing** (context-aware captions)
- Manual or automatic caption input
- Clean GUI built with Tkinter
- Meme preview inside the application
- Output images saved automatically
- Modular, reusable codebase

---

## Why This Project?
This project was built to practice **real software engineering concepts**, not just Python syntax.

Key problems solved:
- Managing project structure and file paths
- Designing logic-driven randomness instead of naive random selection
- Separating UI, logic, and data
- Handling real-world errors and refactoring safely
- Reusing logic across CLI and GUI interfaces

---

## Project Structure
meme-generator/
│
├── data/
│ ├── templates/ # Meme images
│ └── captions.txt # Caption data (grouped logically)
│
├── output/ # Generated memes
│
├── caption_utils.py # Caption loading and pairing logic
├── meme_utils.py # Image and text rendering utilities
├── main.py # CLI version
├── gui.py # GUI version (Tkinter)
├── requirements.txt
└── README.md


---

## Technologies Used
- Python 3
- Pillow (Image Processing)
- Tkinter (GUI)
- OS & Random modules

---

## How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt

2. Run GUI version
python gui.py

3. Run CLI version
python main.py

Learning Outcomes

Python project structuring

Modular programming

Logic-based decision systems

Debugging real runtime errors

Building reusable and scalable code

Future Improvements

Custom font support (Impact-style memes)

Export options

GUI styling improvements

Packaging as a standalone app





