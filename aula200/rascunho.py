import pathlib
from PIL import Image


PATH_IMAGE = pathlib.Path(__file__).parent / "data" / "img" / "dog.jpg"
NEW_IMAGE = pathlib.Path(__file__).parent / "data" / "img" / "new_dog.jpg"

img = Image.open(PATH_IMAGE)
width, height = img.size
exif = img.getexif()

# width    new_width
# height   ??

new_width = 640
new_height = round(height * new_width / width)

print(f"width: {width}, height: {height}")
print(f"width: {new_width}, height: {new_height}")

new_image = img.resize(size=(new_width, new_height))
new_image.save(
    NEW_IMAGE,
    exif=exif,
    optimize=True,
    quality=70,
)
