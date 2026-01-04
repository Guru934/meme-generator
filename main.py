import os
import random
from PIL import Image, ImageDraw, ImageFont
from caption_utils import get_caption_pair, load_captions
from meme_utils import draw_text_with_outline, calculate_text_position

# Load captions
caption_groups = load_captions("data/captions.txt")


# Select template
template_folder = "data/templates"
template_name = random.choice(os.listdir(template_folder))
img = Image.open(f"{template_folder}/{template_name}")
draw = ImageDraw.Draw(img)

# User input
top_input = input("Enter top text (press Enter for auto): ")
bottom_input = input("Enter bottom text (press Enter for auto): ")

top_text, bottom_text = get_caption_pair(caption_groups, top_input,bottom_input)

font = ImageFont.load_default()
width, height = img.size

top_pos = calculate_text_position(draw, top_text, font, width, 10)
bottom_pos = calculate_text_position(draw, bottom_text, font, width, height - 30)

draw_text_with_outline(draw, top_pos, top_text, font)
draw_text_with_outline(draw, bottom_pos, bottom_text, font)

output_file = f"output/meme_{random.randint(1000,9999)}.png"
img.save(output_file)

print("Meme generated successfully")
print("Template:", template_name)
print("Saved as:", output_file)
