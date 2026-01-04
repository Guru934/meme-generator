import tkinter as tk
from PIL import Image, ImageTk
import random
import os

from caption_utils import load_captions, get_caption_pair
from meme_utils import draw_text_with_outline, calculate_text_position

from PIL import ImageDraw, ImageFont

# Load captions
caption_groups = load_captions("data/captions.txt")

# Pick template
def generate_meme():
    template_folder = "data/templates"
    template_name = random.choice(os.listdir(template_folder))
    img = Image.open(f"{template_folder}/{template_name}")

    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    width, height = img.size

    top_input = top_entry.get()
    bottom_input = bottom_entry.get()

    top_text, bottom_text = get_caption_pair(
        caption_groups,
        top_input,
        bottom_input
    )

    top_pos = calculate_text_position(draw, top_text, font, width, 10)
    bottom_pos = calculate_text_position(draw, bottom_text, font, width, height - 30)

    draw_text_with_outline(draw, top_pos, top_text, font)
    draw_text_with_outline(draw, bottom_pos, bottom_text, font)

    output_file = f"output/meme_gui_{random.randint(1000,9999)}.png"
    img.save(output_file)

    # Display image
    img_resized = img.resize((300, 300))
    img_tk = ImageTk.PhotoImage(img_resized)
    image_label.config(image=img_tk)
    image_label.image = img_tk

    status_label.config(text=f"Saved: {output_file}")

# ---------- GUI ----------
root = tk.Tk()
root.title("Meme Generator")

tk.Label(root, text="Top Text").pack()
top_entry = tk.Entry(root, width=40)
top_entry.pack()

tk.Label(root, text="Bottom Text").pack()
bottom_entry = tk.Entry(root, width=40)
bottom_entry.pack()

tk.Button(root, text="Generate Meme", command=generate_meme).pack(pady=10)

image_label = tk.Label(root)
image_label.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
