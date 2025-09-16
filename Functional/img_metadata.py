# note: needs Pillow module
from PIL import Image
from PIL.ExifTags import TAGS

# the image path:
img_path = input("Type the path to the image: ")
img = Image.open(img_path)


def log_metadata():
    exif_data = img.getexif()
    if exif_data:
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            print(f"{tag}: {value}")
    else:
        print("No metadata found!")

def remove_metadata():
    new_img = Image.new(mode = img.mode, size = img.size)
    data = list(img.getdata())
    new_img.putdata(data = data)
    # Saving the new image
    new_img.save(f"Safe.{img.format.lower()}", format=img.format)


# remove_metadata()
# log_metadata()