import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def wrap_text(text, max_width, font, draw):
    lines = []
    for line in text.split("\n"):  
        words = line.split()
        current_line = ""

        for word in words:
            test_line = current_line + " " + word if current_line else word
            bbox = draw.textbbox((0, 0), test_line, font=font)
            text_width = bbox[2] - bbox[0]
            if text_width > max_width:
                lines.append(current_line)
                current_line = word
            else:
                current_line = test_line
        lines.append(current_line)

    return lines

def add_logo(image, logo_path, position):
    logo = cv2.imread(logo_path, cv2.IMREAD_UNCHANGED)
    if logo is None:
        print("Error: Logo not found!")
        return image

    logo_height, logo_width = 150, 400  
    logo = cv2.resize(logo, (logo_width, logo_height))

    y_offset, x_offset = position
    h, w, _ = logo.shape

    if logo.shape[2] == 4:
        alpha = logo[:, :, 3] / 255.0
        for c in range(3):
            image[y_offset:y_offset + h, x_offset:x_offset + w, c] = (
                (1 - alpha) * image[y_offset:y_offset + h, x_offset:x_offset + w, c] + alpha * logo[:, :, c]
            )
    else:
        image[y_offset:y_offset + h, x_offset:x_offset + w] = logo[:, :, :3]

    return image

def calculate_text_height(lines, draw, font, spacing):
    total_height = sum(draw.textbbox((0, 0), line, font=font)[3] for line in lines) + (len(lines) - 1) * spacing
    return total_height

def generate_video(output_path, question, options, duration=15, fps=30, logo_path="logo.png", font_path="Roboto-Regular.ttf"):
    width, height = 1080, 1920  
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    blank_frame = np.zeros((height, width, 3), dtype=np.uint8)

    try:
        font = ImageFont.truetype(font_path, 70)  
        option_font = ImageFont.truetype(font_path, 60)  
    except:
        print("Error: Font not found!")
        font = ImageFont.load_default()
        option_font = ImageFont.load_default()

    pil_image = Image.fromarray(blank_frame)
    draw = ImageDraw.Draw(pil_image)

    text_color = (255, 255, 255)
    margin = 50  
    max_text_width = width - 2 * margin

    question_lines = wrap_text(question, max_text_width, font, draw)
    option_lines = [f"{chr(65 + i)}. {option}" for i, option in enumerate(options)]

    question_height = calculate_text_height(question_lines, draw, font, 20)
    option_height = calculate_text_height(option_lines, draw, option_font, 50)

    total_height = question_height + option_height + 150  
    start_y = (height - total_height) // 2  

    question_start_y = start_y
    option_start_y = question_start_y + question_height + 50  

    for i, line in enumerate(question_lines):
        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]
        x_pos = (width - text_width) // 2
        draw.text((x_pos, question_start_y + i * 100), line, font=font, fill=text_color)

    for i, text in enumerate(option_lines):
        bbox = draw.textbbox((0, 0), text, font=option_font)
        text_width = bbox[2] - bbox[0]
        x_pos = (width - text_width) // 2
        draw.text((x_pos, option_start_y + i * 100), text, font=option_font, fill=text_color)

    blank_frame = np.array(pil_image)

    logo_height = 150  
    y_logo_position = height - 320 - logo_height
    x_logo_position = (width - 400) // 2  

    blank_frame = add_logo(blank_frame, logo_path, (y_logo_position, x_logo_position))

    for _ in range(fps * duration):
        video.write(blank_frame)

    video.release()
    print(f"Video saved at {output_path}")

generate_video('output.mp4', "Predict Output:\nprint(\"abc\" * 3 == 3 * \"abc\")",
               ['True', 'False', 'abcabcabcabcabcabc', 'Error'], 
               logo_path="1_Reels_Generator/logo.png",
               font_path="1_Reels_Generator/Roboto-Variable.ttf")