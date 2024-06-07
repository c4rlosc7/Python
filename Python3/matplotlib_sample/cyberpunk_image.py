from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import numpy as np

# Create a blank image with a black background
width, height = 800, 600
image = Image.new('RGB', (width, height), 'black')
draw = ImageDraw.Draw(image)

# Load a font
try:
    font = ImageFont.truetype("arial.ttf", 40)
except IOError:
    font = ImageFont.load_default()

# Add some neon-colored text
text = "CYBERPUNK"
text_width, text_height = draw.textsize(text, font=font)
text_x = (width - text_width) / 2
text_y = (height - text_height) / 2
draw.text((text_x, text_y), text, font=font, fill="cyan")

# Add some cyberpunk-style graphics
for _ in range(50):
    x1, y1 = np.random.randint(0, width), np.random.randint(0, height)
    x2, y2 = np.random.randint(0, width), np.random.randint(0, height)
    color = tuple(np.random.randint(0, 255, 3))
    draw.line((x1, y1, x2, y2), fill=color, width=2)

# Convert the image to a NumPy array for further manipulation if needed
image_array = np.array(image)

# Display the image using matplotlib
plt.imshow(image_array)
plt.axis('off')  # Hide axes
plt.show()

# Save the image
image.save("cyberpunk_image.png")
