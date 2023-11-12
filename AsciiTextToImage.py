from PIL import Image, ImageDraw, ImageFont

def create_image_from_ascii(ascii_text, output_path="output_image.png", font_size=10):


    font = ImageFont.load_default()
    
    text_lines = ascii_text.split("\n")
    max_line_length = max(len(line) for line in text_lines)
    image_width = max_line_length * font_size
    image_height = len(text_lines) * font_size

    # Create a new image
    image = Image.new("RGB", (image_width, image_height), color="white")
    draw = ImageDraw.Draw(image)

    # Draw the ASCII text on the image
    y_position = 0
    for line in text_lines:
        draw.text((0, y_position), line, font=font, fill="black")
        y_position += font_size

    
    image.save(output_path)


with open("ascii_text.txt", "r") as f:
    ascii_text = f.read()
    
#change font_size to check better view
create_image_from_ascii(ascii_text, "Ascii_image.png", font_size=10)

