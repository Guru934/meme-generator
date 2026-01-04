from PIL import ImageDraw

def draw_text_with_outline(draw, position, text, font):
    x, y = position
    for dx in range(-2, 3):
        for dy in range(-2, 3):
            draw.text((x + dx, y + dy), text, font=font, fill="black")
    draw.text((x, y), text, font=font, fill="white")


def calculate_text_position(draw, text, font, image_width, y_pos):
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    return ((image_width - text_width) // 2, y_pos)
